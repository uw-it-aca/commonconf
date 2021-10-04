# Copyright 2021 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

import os
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
            try:
                return os.environ[key]
            except KeyError:
                raise AttributeError(
                    "Key {} not in section {} or in environment variables"
                    .format(key, self.section))
