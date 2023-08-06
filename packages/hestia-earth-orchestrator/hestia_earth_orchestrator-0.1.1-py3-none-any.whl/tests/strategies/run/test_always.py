import unittest

from hestia_earth.orchestrator.strategies.run.always import should_run


class TestStrategiesRunAlways(unittest.TestCase):
    def test_should_run(self):
        self.assertEqual(should_run({}, {}), True)
