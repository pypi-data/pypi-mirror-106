from hestia_earth.schema import SiteSiteType, TermTermType
from hestia_earth.utils.lookup import download_lookup, _get_single_table_value, column_name
from hestia_earth.utils.tools import list_sum, safe_parse_float
from hestia_earth.utils.model import filter_list_term_type, find_term_match

from hestia_earth.models.log import logger
from hestia_earth.models.utils.indicator import _new_indicator
from hestia_earth.models.utils.impact_assessment import get_product
from hestia_earth.models.utils.input import get_total_value
from . import MODEL

TERM_ID = 'scarcityWeightedWaterUse'
AWARE_KEY = 'awareWaterBasinId'
IRRIGATED_SITE_TYPES = [
    SiteSiteType.CROPLAND.value,
    SiteSiteType.PERMANENT_PASTURE.value
]


def _indicator(value: float):
    logger.info('model=%s, term=%s, value=%s', MODEL, TERM_ID, value)
    indicator = _new_indicator(TERM_ID, MODEL)
    indicator['value'] = value
    return indicator


def _get_annual_characterization_factor(impact_assessment: dict):
    site = impact_assessment.get('site', impact_assessment.get('cycle', {}).get('site', {}))
    aware_value = site.get(AWARE_KEY)
    lookup_col = 'YR_IRRI' if site.get('siteType') in IRRIGATED_SITE_TYPES else 'YR_NONIRRI'
    return safe_parse_float(
        _get_single_table_value(
            download_lookup(f"{AWARE_KEY}.csv", True), column_name(AWARE_KEY), int(aware_value), column_name(lookup_col)
        ), None
    ) if aware_value else None


def _run(irrigation: float, seed: float, pyield: float, awarecf: float, economic_value: float):
    value = (irrigation / pyield) * (seed / (seed + pyield)) * economic_value / 100 * awarecf
    return [_indicator(value)]


def _should_run(impact_assessment: dict):
    inputs = impact_assessment.get('cycle', {}).get('inputs', [])

    filter_irrigation = filter_list_term_type(inputs, TermTermType.WATER)
    irrigation = list_sum(get_total_value(filter_irrigation))

    seed = list_sum(find_term_match(inputs, 'seed').get('value', []))

    product = get_product(impact_assessment)
    pyield = list_sum(product.get('value', [])) if product else 0
    economic_value = product.get('economicValueShare') if product else None

    awarecf = _get_annual_characterization_factor(impact_assessment)

    logger.debug('irrigation=%s, seed=%s, yield=%s, awarecf=%s', irrigation, seed, pyield, awarecf)

    should_run = irrigation > 0 \
        and seed > 0 \
        and pyield > 0 \
        and awarecf is not None \
        and economic_value is not None
    logger.info('should_run=%s', should_run)
    return should_run, irrigation, seed, pyield, awarecf, economic_value


def run(impact_assessment: dict):
    should_run, irrigation, seed, pyield, awarecf, economic_value = _should_run(impact_assessment)
    return _run(irrigation, seed, pyield, awarecf, economic_value) if should_run else []
