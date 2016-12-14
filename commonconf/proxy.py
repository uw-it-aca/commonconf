from commonconf.exceptions import NotConfigured


class ConfProxy(object):
    backend = None

    def __getattr__(self, key):
        backend = self.get_backend()

        return backend.get(key)

    def get_backend(self):
        if not ConfProxy.backend:
            raise NotConfigured("Must configure a commonconf backend")

        return ConfProxy.backend
