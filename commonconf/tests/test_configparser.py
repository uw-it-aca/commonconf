# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
import unittest
from commonconf.backends import use_configparser_backend
from commonconf import settings
import os

my_dir = os.path.dirname(__file__)
config_path = os.path.join(my_dir, "files", "sections.cfg")


class TestConfigParserBackend(unittest.TestCase):
    def test_valid(self):
        use_configparser_backend(config_path, "Section1")

        value = settings.DEBUG

    def test_invalid(self):
        use_configparser_backend(config_path, "Section1")

        with self.assertRaises(Exception):
            settings.MISSING_KEY_FOR_TESTING

    def test_default_value(self):
        use_configparser_backend(config_path, "Section1")

        value = getattr(settings, "MISSING_KEY_FOR_TESTING", "OK")
        self.assertEqual(value, "OK")
