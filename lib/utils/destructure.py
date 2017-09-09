def destructure(d):
    ''' Destructures a dictionary. '''
    def destructureArgs(*args):
        return [d[k] for k in args]

    return destructureArgs
