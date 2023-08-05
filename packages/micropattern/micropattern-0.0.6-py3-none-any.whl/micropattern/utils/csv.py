from itertools import islice, zip_longest
import csv


def read_csv_data_chunk(file_path, csv_headers, data_row=2, chunk_size=1000, encoding='utf-8'):
    """
        Lazy read csv file with chunk_size and select data base on column names
    """

    def jump_to_data_row_of_chunk():
        try:
            next(islice(reader, data_row - 2, None))  # jump to before data row
        except StopIteration:
            raise ValueError('Invalid data row input {}'.format(data_row))

    if data_row < 2:
        raise ValueError('No data found at row {}'.format(data_row))

    with open(file_path, encoding=encoding) as f:
        reader = csv.reader(f, csv.excel)
        jump_to_data_row_of_chunk()
        result = []
        for line in reader:
            row = dict(zip_longest(csv_headers, line))
            result.append(row)
            if len(result) == chunk_size:
                yield result
                result = []
        if len(result) > 0:  # in case size of last chunk is less than chunk size
            yield result


def read_csv_header(file_path, header_row=1, encoding='utf-8'):
    """
        Read the headers of csv file.
    """
    if header_row < 1:
        raise ValueError('Header row must be greater than or equals 1 , value={}'.format(header_row))
    with open(file_path, encoding=encoding) as f:
        reader = csv.reader(f, csv.excel)
        try:
            return next(islice(reader, header_row - 1, None))
        except StopIteration:
            raise ValueError('Can\'t find header row at line {}'.format(header_row))
