class Anchor():

    def __init__(self):
        ''' Initialize our plugin pool. '''
        self._plugins = {}


    def apply_plugins(self, event, *args, **kwargs):
        ''' Apply plugins registered for a event. '''
        if isinstance(event, list):
            for n in event:
                self.apply_plugins(n, args, kwargs)
            return

        if not self._plugins[event]:
            return
        plugins = self._plugins[event]
        for plugin in plugins:
            plugin(*args, **kwargs)


    def has_plugins(self, event):
        ''' Check if any plugins are registered to a event. '''
        if event not in self._plugins:
            return False
        plugins = self._plugins[event]

        return len(plugins)


    def plugin(self, event, fn):
        ''' Register a plugin under a event. '''
        if isinstance(event, list):
            for n in event:
                self.plugin(n, fn)
            return
        if event not in self._plugins:
            self._plugins[event] = [fn]
        else:
            self._plugins[event].append(fn)


    def apply(self, *args):
        ''' Attaches the plugins to the instance. '''
        for arg in args:
            arg.apply(self)
