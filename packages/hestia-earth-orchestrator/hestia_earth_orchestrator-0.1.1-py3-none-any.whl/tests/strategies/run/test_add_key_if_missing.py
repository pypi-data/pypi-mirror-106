import unittest

from hestia_earth.orchestrator.strategies.run.add_key_if_missing import should_run


class TestStrategiesRunAddKeyIfMissing(unittest.TestCase):
    def test_should_run(self):
        data = {}
        key = 'model-key'
        model = {'key': key}

        # key not in data => run
        self.assertEqual(should_run(data, model), True)

        # key in data => no run
        data[key] = 10
        self.assertEqual(should_run(data, model), False)
