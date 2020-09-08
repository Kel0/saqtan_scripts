import logging
import re
from typing import Dict, List, Optional, Union

import requests

from .utils import read_json_file

logger = logging.getLogger(__name__)

FEATURES_ATTR_TYPE = Dict[str, Union[str, int, float]]
FEATURES_TYPE = List[Dict[str, FEATURES_ATTR_TYPE]]


def handle_post_data(
    year: int, period: Optional[int] = None, city_code: Optional[int] = None
) -> Dict[str, str]:
    post_dicts: Dict[str, Dict[str, str]] = read_json_file(
        "saqtan_scripts/Resources/get_crimes_post_data.json"
    )
    if period is None:
        post_dicts["post_data_with_yr_city"]["where"] = post_dicts[
            "post_data_with_yr_city"
        ]["where"].format(year, city_code)
        return post_dicts["post_data_with_yr_city"]

    elif city_code is None:
        post_dicts["post_data_with_yr_period"]["where"] = post_dicts[
            "post_data_with_yr_period"
        ]["where"].format(year, period)
        return post_dicts["post_data_with_yr_period"]

    post_dicts["post_data_with_yr_period_city"]["where"] = post_dicts[
        "post_data_with_yr_period_city"
    ]["where"].format(year, period, city_code)
    return post_dicts["post_data_with_yr_period_city"]


def get_crimes(
    year: int, period: Optional[int] = None, city_code: Optional[int] = None
) -> Dict[str, List[Dict[str, Union[str, int, float]]]]:
    crimes: Dict[str, List[Dict[str, Union[str, int, float]]]] = {"attrs": []}
    crimes_url: str = read_json_file("saqtan_scripts/Resources/api_urls.json")[
        "crimes_url"
    ]
    post_data: Dict[str, str] = handle_post_data(
        year=year, period=period, city_code=city_code
    )
    response: requests.Response = requests.post(url=crimes_url, data=post_data)
    features: FEATURES_TYPE = response.json()["features"]
    for data in features:
        attributes: FEATURES_ATTR_TYPE = data["attributes"]
        geo_location: FEATURES_ATTR_TYPE = data["geometry"]

        attributes.update({"x": geo_location["x"], "y": geo_location["y"]})
        crimes["attrs"].append(attributes)

    return crimes


def handle_crime_code(
    crime_code: List[str], fetched_row: Dict[str, str]
) -> Optional[Dict[str, str]]:
    if len(crime_code) > 0:
        for code in crime_code:
            if len(str(code)) > 1 or "гл." in code:
                if "гл." in code:
                    code_for_return = code.split(".")[-1].strip()
                else:
                    code_for_return = code

                return {
                    "stat": code_for_return,
                    "crime_desc": fetched_row["CRIME_ID_DESC"],
                }
    return None


def get_crime_ids() -> Optional[List[Dict[str, str]]]:
    """Get crime ids which set by arcgis"""
    crimes_arr: List[Dict[str, str]] = []
    crime_ids_url: str = read_json_file("saqtan_scripts/Resources/api_urls.json")[
        "crime_ids_url"
    ]

    response: requests.Response = requests.get(url=crime_ids_url)

    if response.status_code == 200:
        for data in response.json()["list"]:
            if "ст." in data["CRIME_ID_DESC"] or "гл." in data["CRIME_ID_DESC"]:
                match_crime_codes: List[str] = re.findall(
                    r"([\d]{1,}|гл.\d+|гл.\s\d+)", data["CRIME_ID_DESC"]
                )
                crime_code: Optional[Dict[str, str]] = handle_crime_code(
                    crime_code=match_crime_codes, fetched_row=data
                )
                if crime_code is None:  # pragma: no cover
                    continue
                crimes_arr.append(crime_code)

        return crimes_arr
    else:  # pragma: no cover
        logger.warning(
            f"Failed request for {crime_ids_url}. Status code: {response.status_code}"
        )
        return None
