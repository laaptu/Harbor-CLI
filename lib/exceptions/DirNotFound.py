class DirNotFoundException(Exception):
    ''' Custom exception class whenever a file is not found. '''
    def __init__(self, path):
        super().__init__("Directory {0} does not exist.".format(path))

        self.path = path
