import sys
import unittest
from commonconf.test.django import TestDjangoBackend
from commonconf.test.configparser import TestConfigParserBackend

suite = unittest.TestSuite()

for case in (TestDjangoBackend, TestConfigParserBackend):
    tests = unittest.TestLoader().loadTestsFromTestCase(case)
    suite.addTests(tests)
value = unittest.TextTestRunner(verbosity=1).run(suite)

if len(value.errors) or len(value.failures):
    sys.exit(1)

sys.exit(0)


