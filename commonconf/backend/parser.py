from configparser import RawConfigParser, NoOptionError


class ConfigParserBackend(object):
    def __init__(self, path, section):
        self.config = config = RawConfigParser()
        self.config.read(path)
        self.section = section

    def get(self, key):
        try:
            return self.config.get(self.section, key)
        except NoOptionError as ex:
            raise AttributeError(
                "Key {} not in section {}".format(key, self.section))
