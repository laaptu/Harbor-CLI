class Anchor():

    def __init__(self):
        ''' Initialize our plugin pool. '''
        self._plugins = {}


    def apply_plugins(self, name, *args, **kwargs):
        ''' Apply plugins registered for a name. '''
        if not self._plugins[name]:
            return

        plugins = self._plugins[name]
        for plugin in plugins:
            plugin(*args, **kwargs)


    def has_plugins(self, name):
        ''' Check if any plugins are registered to a name. '''
        if name not in self._plugins:
            return False
        plugins = self._plugins[name]

        return len(plugins)


    def plugin(self, name, fn):
        ''' Register a plugin under a name. '''
        if isinstance(name, list):
            for n in name:
                self.plugin(n, fn)
            return
        if name not in self._plugins:
            self._plugins[name] = [fn]
        else:
            self._plugins[name].append(fn)

        print('Just registered plugin ', fn)
        print('Staate is now: ', self._plugins)


    def apply(self, *args):
        ''' Attaches the plugins to the instance. '''
        for arg in args:
            arg.apply(self)
