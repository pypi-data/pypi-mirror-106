# micropattern
Common package
```sh
pip install micropattern
```  
Distribute package to PYPI  
1. Update new version in `setup.py`
```python
setuptools.setup(
    name='micropattern',
    version="0.0.4",
```  
2. Push or merge to `release` branch
3. Check distributing process in [Action](https://github.com/MicroPattern/micropattern/actions/workflows/main.yaml)
### Using Rabbit MQ `basic_publish` with helper
```python
from micropattern.utils.mq import BasicPublish
 queue = BasicPublish(
     host=MQ_HOST,
     port=MQ_PORT,
     username=MQ_USERNAME,
     password=MQ_PASSWORD,
     queue_name='test_queue',
     debug=True
 )

 with queue() as publisher:
     publisher.enqueue("{'test': 'test'}")
```

### Using remote config with `Registry` helper

1. Add `MP_REGISTRY_HOST=10.15.0.7`, `MP_REGISTRY_PORT=8000` to your environment first.  

2. Define your configs manually with UI: [`http://10.15.0.7:8000`](http://10.15.0.7:8000)  
   E.g. `dummy` configs
   ```json
    {
       "name": "Hai Tran",
       "phone": 1234567890
    }
    ```
3. Map your config to a class inherited `Registry`
   ```python
   from micropattern.registry import Registry
   class DummyConfig(Registry):
        name: str
        phone: int
        def __init__(self):
            super().__init__(key='dummy')
   ```

4. Create an instance of config, and just `dot` attribute, your remote configs will be loaded to the instance
   ```python
   dummy_cfg = DummyConfig()
   print(dummy_cfg.name)
   print(dummy_cfg.phone)
   ```

5. Save remote configs, your configs automatically submitted after leaving the context
   ```python
   with dummy_cfg() as cfg:
       cfg.name = 'New name'
       cfg.phone = 987654321
   ```

### CSV utilities:
Support lazy load csv file.
Default header row starts at row #1 and data row starts at row #2 of csv file.
```python
from utils.csv import read_csv_data_chunk, read_csv_header

csv_headers = read_csv_header(file_path, header_row=1)
for data in read_csv_data_chunk(file_path, csv_headers, data_row=2):
    #do_something(data)
```
