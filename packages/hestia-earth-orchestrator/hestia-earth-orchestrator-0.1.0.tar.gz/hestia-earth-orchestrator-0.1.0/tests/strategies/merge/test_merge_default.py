import unittest

from hestia_earth.orchestrator.strategies.merge.merge_default import merge


class TestStrategiesMergeDefault(unittest.TestCase):
    def test_should_merge(self):
        source = {'value': [100]}
        dest = {'value': [50]}
        self.assertEqual(merge(source, dest), dest)
