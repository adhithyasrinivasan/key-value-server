from functools import lru_cache

DATA_FILE_PATH = 'input.data'

@lru_cache(maxsize=None)
def read_data_file():
    """
    Read key-value pairs from the data file and cache the result.

    Returns:
        dict: A dictionary containing key-value pairs read from the file.
    """
    key_value_pairs = {}
    with open(DATA_FILE_PATH, 'r') as file:
        for line in file:
            # Split the line into key and value
            key, value = line.strip().split(' ', 1)
            key_value_pairs[key] = value
    return key_value_pairs