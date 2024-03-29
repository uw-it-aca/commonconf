# Copyright 2024 UW-IT, University of Washington
# SPDX-License-Identifier: Apache-2.0

from __future__ import absolute_import
import unittest
from commonconf.backends import use_configparser_backend
from commonconf import settings, override_settings
import os

my_dir = os.path.dirname(__file__)
config_path = os.path.join(my_dir, "files", "sections.cfg")


class TestOverrides(unittest.TestCase):
    def test_decorator(self):
        use_configparser_backend(config_path, "Section1")
        self.assertTrue(settings.DEBUG)

        with self.assertRaises(Exception):
            settings.OTHER

        @override_settings(DEBUG="What!", OTHER="Also")
        def get_overridden():
            return settings.DEBUG, settings.OTHER

        debug, other = get_overridden()
        self.assertEqual(debug, "What!")
        self.assertEqual(other, "Also")

        self.assertTrue(settings.DEBUG)

        with self.assertRaises(Exception):
            settings.OTHER

    def test_context(self):
        use_configparser_backend(config_path, "Section1")
        self.assertTrue(settings.DEBUG)

        with self.assertRaises(Exception):
            settings.OTHER

        with override_settings(DEBUG="What!", OTHER="Also"):
            debug = settings.DEBUG
            other = settings.OTHER

        self.assertEqual(debug, "What!")
        self.assertEqual(other, "Also")

        self.assertTrue(settings.DEBUG)

        with self.assertRaises(Exception):
            settings.OTHER


@override_settings(DEBUG="class level", OTHER="More")
class TestClassOverride(unittest.TestCase):
    def test_it(self):
        self.assertEqual(settings.DEBUG, "class level")
        self.assertEqual(settings.OTHER, "More")

    def test_bad_superclass(self):
        with self.assertRaises(Exception):
            @override_settings()
            class BadWrap(object):
                pass
