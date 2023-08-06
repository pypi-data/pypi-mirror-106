from hestia_earth.utils.api import download_hestia
from hestia_earth.utils.model import find_term_match
from hestia_earth.utils.tools import list_average


def _get_term_type_completeness(cycle: dict, term):
    term_type = (download_hestia(term) if isinstance(term, str) else term).get('termType')
    return cycle.get('dataCompleteness', {}).get(term_type, False)


def _is_term_type_complete(cycle: dict, term):
    return _get_term_type_completeness(cycle, term) is True


def _is_term_type_incomplete(cycle: dict, term):
    return _get_term_type_completeness(cycle, term) is False


def get_land_occupation(cycle: dict):
    measurements = cycle.get('site', {}).get('measurements', [])
    fallowCorrection = find_term_match(measurements, 'fallowCorrection').get('value', [])
    return cycle.get('cycleDuration', 365) / 365 * list_average(fallowCorrection) if len(fallowCorrection) > 0 \
        else None
