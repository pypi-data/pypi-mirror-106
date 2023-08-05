import abc
import json
import time
from multiprocessing import Process, Manager
from threading import Thread
from typing import List, Optional, Dict

from .logger import Logger


class ParallelFn(abc.ABC):
    @abc.abstractmethod
    def apply(self, worker_name, log_fn, **kwargs) -> List:
        raise NotImplementedError()


class ParallelFnExecutor:
    def __init__(self, name, num_worker, use_thread=False, debug=False):
        self.name = name
        self.worker_count = num_worker
        self.__logger = Logger(f'{name}_executor') if debug else None
        self.__file_proxy: Optional[List] = None
        self.__use_thread = use_thread
        self.__fn_cls = None
        self.__debug = debug

    def log(self, message, error=False):
        if self.__logger is None:
            return
        if error:
            self.__logger.error(message)
        else:
            self.__logger.info(message)

    def __execute_job(self, worker_name, params):
        self.log(f"[{worker_name}] Started")

        start_ts = time.time()

        # execute fn
        data = self.__fn_cls().apply(worker_name, lambda msg: self.log(f'[{worker_name}]{msg}'), **params)

        # save result
        file_name = f"/tmp/{time.time()}_{worker_name}.json"
        with open(file_name, "w") as wd:
            wd.write(json.dumps(data, separators=(',', ':')))
        self.__file_proxy.append(file_name)

        end_ts = time.time()

        self.log(f"[{worker_name}] Done in {end_ts - start_ts:.2f}s")

    @property
    def __process_keys(self):
        for i in range(self.worker_count):
            yield f"{self.name}_exec_proc_{i}"

    def __split_jobs(self, static_params: Dict, dynamic_params: Dict):
        params = {**static_params}
        job_args = {}
        for k, v in dynamic_params.items():
            task_count = int(len(v) / self.worker_count)
            for i, proc in enumerate(self.__process_keys):
                values = v[i * task_count:] if i == self.worker_count - 1 else v[i * task_count:(i + 1) * task_count]
                if proc in job_args:
                    job_args[proc][k] = values
                else:
                    job_args[proc] = {k: values}
        for k, v in job_args.items():
            v.update(params)
        return job_args

    def __start_workers(self, params: Dict):
        worker_pool = []
        executor = Thread if self.__use_thread else Process
        for proc in self.__process_keys:
            proc = executor(target=self.__execute_job, args=(proc, params[proc]))
            proc.start()
            worker_pool.append(proc)
        for proc in worker_pool:
            proc.join()

    def __merge_result(self) -> List:
        result = []
        for file in self.__file_proxy:
            with open(file, "r") as rd:
                try:
                    result.extend(json.loads(rd.read()))
                except Exception as e:
                    self.log(f"Failed to read result {file}: {str(e)}", error=True)
        return result

    def execute(self, fn, static_params: Optional[Dict] = None, params: Optional[Dict] = None) -> List:
        self.__file_proxy = Manager().list()
        self.__fn_cls = fn
        self.__start_workers(self.__split_jobs(static_params, params))
        return self.__merge_result()
