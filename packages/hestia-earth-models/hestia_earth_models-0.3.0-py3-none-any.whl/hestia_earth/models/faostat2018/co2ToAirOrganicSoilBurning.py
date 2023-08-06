from hestia_earth.schema import EmissionMethodTier
from hestia_earth.utils.model import find_primary_product

from hestia_earth.models.log import logger
from hestia_earth.models.utils.emission import _new_emission
from hestia_earth.models.utils.cycle import get_land_occupation
from hestia_earth.models.utils.crop import get_crop_grouping, get_emission_factor, TONNE_TO_KG
from . import MODEL

TERM_ID = 'co2ToAirOrganicSoilBurning'


def _emission(value: float):
    logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
    emission = _new_emission(TERM_ID, MODEL)
    emission['value'] = [value]
    emission['methodTier'] = EmissionMethodTier.TIER_1.value
    return emission


def _run(land_occupation: float, factors: list):
    value = land_occupation * sum(factors) / TONNE_TO_KG
    return [_emission(value)]


def _should_run(cycle: dict):
    site = cycle.get('site', {})
    country_id = site.get('country', {}).get('@id')

    land_occupation = get_land_occupation(cycle)
    primary_product = find_primary_product(cycle)
    crop_grouping = get_crop_grouping(primary_product.get('term', {}).get('@id')) if primary_product else None
    logger.debug('land_occupation=%s, crop_grouping=%s', land_occupation, crop_grouping)

    co2ch4n2o_landuse_burning = get_emission_factor(
        factor='co2ch4n2olanduseburning',
        term_id=country_id,
        lookup_col=crop_grouping) if country_id and crop_grouping else None

    ch4n2o_landuse = get_emission_factor(
        factor='ch4n2olanduse',
        term_id=country_id,
        lookup_col=crop_grouping) if country_id and crop_grouping else None

    factors = [co2ch4n2o_landuse_burning, ch4n2o_landuse]

    should_run = land_occupation is not None and all([factor is not None for factor in factors])
    logger.info('model=%s, term=%s, should_run=%s', MODEL, TERM_ID, should_run)
    return should_run, land_occupation, factors


def run(cycle: dict):
    should_run, land_occupation, factors = _should_run(cycle)
    return _run(land_occupation, factors) if should_run else []
