import sys
import unittest
from commonconf.test.django import TestDjangoBackend
from commonconf.test.configparser import TestConfigParserBackend
from commonconf.test.override import TestOverrides, TestClassOverride

suite = unittest.TestSuite()

cases = (TestDjangoBackend, TestConfigParserBackend, TestOverrides,
         TestClassOverride)

for case in cases:
    tests = unittest.TestLoader().loadTestsFromTestCase(case)
    suite.addTests(tests)
value = unittest.TextTestRunner(verbosity=1).run(suite)

if len(value.errors) or len(value.failures):
    sys.exit(1)

sys.exit(0)


