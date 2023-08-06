from hestia_earth.schema import EmissionMethodTier, TermTermType
from hestia_earth.utils.lookup import column_name, download_lookup, get_table_value
from hestia_earth.utils.model import filter_list_term_type, find_primary_product
from hestia_earth.utils.tools import list_sum, safe_parse_float

from hestia_earth.models.log import logger
from hestia_earth.models.utils import _filter_list_term_unit
from hestia_earth.models.utils.constant import Units
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.property import get_node_property
from . import MODEL

TERM_ID = 'ch4ToAirEntericFermentation'


def _emission(value: float):
    logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_2.value
    return emission


def _get_input_feed(input: dict):
    term_id = input.get('term', {}).get('@id')
    lookup = download_lookup('crop.csv', True)
    energy_comp_value = safe_parse_float(
        get_table_value(lookup, 'termid', term_id, column_name('energyContentOfDryMatter'))
    ) if term_id else 0
    property = get_node_property(input, 'dryMatter')
    property_value = property.get('value') if property else 0
    return list_sum(input.get('value', [])) * property_value * energy_comp_value


def _get_feed(cycle: dict):
    inputs = _filter_list_term_unit(cycle.get('inputs', []), Units.KG)
    inputs = (
        filter_list_term_type(inputs, TermTermType.CROP) +
        filter_list_term_type(inputs, TermTermType.OTHER)
    )
    return list_sum([_get_input_feed(input) for input in inputs])


def _run(feed_data: float, primary_product: dict):
    term_id = primary_product.get('term', {}).get('@id')
    lookup = download_lookup('animalProduct.csv', True)
    enteric_fermentation_factor = safe_parse_float(
        get_table_value(lookup, 'termid', term_id, column_name('Enteric fermentation emissions factor'))
    )
    logger.debug('enteric_fermentation_factor=%s', enteric_fermentation_factor)
    value = feed_data * enteric_fermentation_factor
    return [_emission(value)]


def _should_run(cycle: dict):
    primary_product = find_primary_product(cycle)
    feed_data = _get_feed(cycle)
    should_run = all([feed_data, primary_product])
    logger.info('model=%s, term=%s, should_run=%s', MODEL, TERM_ID, should_run)
    return should_run, feed_data, primary_product


def run(cycle: dict):
    should_run, feed_data, primary_product = _should_run(cycle)
    return _run(feed_data, primary_product) if should_run else []
