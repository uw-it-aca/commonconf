from commonconf.proxy import ConfProxy


class override_settings(object):
    def __init__(self, *args, **kwargs):
        self.overrides = kwargs

    def __call__(self, func, *args, **kwargs):
        def wrapped(*args, **kwargs):
            try:
                self.__enter__()
                value = func(*args, **kwargs)
            finally:
                self.__exit__()
            return value
        return wrapped

    def __enter__(self, *args, **kwargs):
        ConfProxy.set_overrides(self.overrides)

    def __exit__(*args, **kwargs):
        ConfProxy.clear_overrides()
