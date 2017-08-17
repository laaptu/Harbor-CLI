def with_credentials(**kwargs):
    ''' Wraps any function f with some credential data as kwargs. '''
    def run_with_credentials(f):
        def wrapper(*args, **kwargs):
            f(*args, **kwargs)
        return wrapper

    return run_with_credentials
