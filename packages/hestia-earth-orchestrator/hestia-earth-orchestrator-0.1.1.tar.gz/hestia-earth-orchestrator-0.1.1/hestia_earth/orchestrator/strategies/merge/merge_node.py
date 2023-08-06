import pydash

from hestia_earth.orchestrator.log import logger
from hestia_earth.orchestrator.utils import update_node_version, _average

METHOD_TIER_ORDER = [
    'tier 1',
    'tier 2',
    'tier 3',
    'measured',
    'background'
]


def _has_threshold_diff(source: dict, dest: dict, key: str, threshold: float):
    source_value = _average(source.get(key), None)
    dest_value = _average(dest.get(key), None)
    diff = None if source_value is None or dest_value is None else abs(source_value - dest_value)
    logger.debug('merge %s with threshold=%s, current diff=%s', key, threshold, diff)
    return diff is None or \
        (source_value == 0 and diff > threshold) or \
        (source_value != 0 and diff / source_value > threshold)


def _should_merge_threshold(source: dict, dest: dict, args: dict):
    [key, threshold] = args.get('replaceThreshold', [None, 0])
    return True if key is None else _has_threshold_diff(source, dest, key, threshold)


def _should_merge_lower_tier(source: dict, dest: dict, args: dict):
    should_replace = args.get('replaceLowerTier', False)
    source_tier = METHOD_TIER_ORDER.index(source.get('methodTier', METHOD_TIER_ORDER[0]))
    dest_tier = METHOD_TIER_ORDER.index(dest.get('methodTier', METHOD_TIER_ORDER[-1]))
    return True if should_replace else dest_tier > source_tier


_MERGE_FROM_ARGS = {
    'replaceThreshold': _should_merge_threshold,
    'replaceLowerTier': _should_merge_lower_tier
}


def _should_merge_args(source: dict, dest: dict, args: dict):
    return all([func(source, dest, args) for func in _MERGE_FROM_ARGS.values()])


def merge(source: dict, dest: dict, version: str, args={}):
    should_merge = source is None or _should_merge_args(source, dest, args)
    return update_node_version(version, pydash.objects.merge({}, source, dest), source) if should_merge else source
