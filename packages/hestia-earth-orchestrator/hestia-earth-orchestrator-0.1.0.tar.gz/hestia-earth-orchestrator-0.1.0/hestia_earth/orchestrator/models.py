import importlib
from functools import reduce
from concurrent.futures import ThreadPoolExecutor
from pydash.objects import clone_deep

from .log import logger
from .version import VERSION
from .utils import get_required_model_param, _snakecase
from .strategies.run import should_run
from .strategies.merge import merge


def _import_model(name: str):
    # try to load the model from the default hestia library, fallback to fully specified name
    try:
        return {
            'run': importlib.import_module(f"hestia_earth.models.{name}").run,
            'version': importlib.import_module('hestia_earth.models.version').VERSION
        }
    except ModuleNotFoundError:
        return {
            'run': importlib.import_module(f"{name}").run,
            'version': VERSION
        }


def _run_pre_checks(data: dict):
    node_type = _snakecase(data['@type'])
    try:
        pre_checks = _import_model('.'.join([node_type, 'pre_checks'])).get('run')
        logger.info('running pre checks for %s', node_type)
        return pre_checks(data)
    except Exception:
        return data


def _run_post_checks(data: dict):
    node_type = _snakecase(data['@type'])
    try:
        post_checks = _import_model('.'.join([node_type, 'post_checks'])).get('run')
        logger.info('running post checks for %s', node_type)
        return post_checks(data)
    except Exception:
        return data


def _run_model(data: dict, model: dict):
    module = _import_model(get_required_model_param(model, 'model'))
    result = module.get('run')(get_required_model_param(model, 'value'), data)
    return {'data': data, 'model': model, 'version': module.get('version'), 'result': result}


def _run(data: dict, model: dict):
    return _run_model(data, model) if should_run(data, model) else None


def _run_serie(data: dict, models: list):
    return reduce(
        lambda prev, m: merge(prev, _run_parallel(prev, m) if isinstance(m, list) else [_run(prev, m)]),
        models,
        data
    )


def _run_parallel(data: dict, models: list):
    with ThreadPoolExecutor() as executor:
        return list(executor.map(lambda model: _run(clone_deep(data), model), models))


def run(data: dict, models: list):
    # run pre-checks if exist
    data = _run_pre_checks(data)
    data = _run_serie(data, models)
    # run post-checks if exist
    return _run_post_checks(data)
