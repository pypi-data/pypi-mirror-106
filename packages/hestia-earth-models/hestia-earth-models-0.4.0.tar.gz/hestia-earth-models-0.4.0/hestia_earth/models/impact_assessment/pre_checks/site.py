from hestia_earth.schema import SchemaType

from hestia_earth.models.utils import _load_calculated_node


def _get_site(impact: dict): return _load_calculated_node(impact.get('site', {}), SchemaType.SITE)


def _should_run(impact: dict):
    site_id = impact.get('site', {}).get('@id')
    run = site_id is not None
    return run


def run(impact: dict):
    impact['site'] = _get_site(impact) if _should_run(impact) else impact.get('site')
    return impact
