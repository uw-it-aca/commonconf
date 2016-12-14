import unittest
from commonconf.test.django import TestDjangoBackend
from commonconf.test.configparser import TestConfigParserBackend

suite = unittest.TestSuite()

for case in (TestDjangoBackend, TestConfigParserBackend):
    tests = unittest.TestLoader().loadTestsFromTestCase(case)
    suite.addTests(tests)
unittest.TextTestRunner(verbosity=1).run(suite)


