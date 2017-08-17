import os
from functools import wraps

from lib.exceptions.FileNotFound import FileNotFoundException

def requires_presence_of_file(file_path):
    ''' Decorator to verify if a file exists before doing anything else. '''
    def wrapper(f):
        @wraps(f)
        def with_args(*args, **kwargs):
            if not os.path.isfile(file_path):
                raise FileNotFoundException(file_path)

            return f(*args, **kwargs)
        return with_args
    return wrapper
