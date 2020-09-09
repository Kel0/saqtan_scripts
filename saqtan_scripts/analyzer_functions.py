import logging
from datetime import datetime
from typing import Dict, List, Optional, Union

from sqlalchemy.orm import Session

from .database.db import session
from .database.models import CityCodes, CrimeCodes, Features

logger = logging.getLogger(__name__)


def get_crime_types_count(year: int) -> List[Dict[str, Union[str, int]]]:
    sqlalchemy_session: Session = session()

    crimes_arr: List[Dict[str, Union[str, int]]] = []
    crime_codes: List[CrimeCodes] = sqlalchemy_session.query(CrimeCodes).all()

    for crime_code in crime_codes:
        crime_code_formatted: str = "0"
        if len(str(crime_code.crime_code)) == 2:
            crime_code_formatted = f"0{crime_code.crime_code}0"
        elif len(str(crime_code.crime_code)) == 3:
            crime_code_formatted = f"{crime_code.crime_code}0"

        features_count: int = (
            sqlalchemy_session.query(Features)
            .filter(Features.year == year)
            .filter(Features.crime_code == crime_code_formatted)
            .count()
        )
        crime_desc: str = crime_code.crime_desc.split("(")[0]

        if features_count > 0:
            logger.info(  # pragma: no cover
                f"Count crimes: {features_count} | crime_code: {crime_code_formatted} | year: {year}"
            )
            crimes_arr.append(
                {
                    "year": year,
                    "crime_code": crime_code.crime_code,
                    "crime_desc": crime_desc,
                    "crime_count": features_count,
                }
            )

    return crimes_arr


def get_crimes_count() -> List[List[Union[int, float]]]:
    crimes_count_info: List[List[Union[int, float]]] = []
    sqlalchemy_session: Session = session()
    now = datetime.now()

    for yr in range(now.year - 4, now.year + 1):
        features = (
            sqlalchemy_session.query(Features).filter(Features.year == yr).count()
        )
        crimes_count_info.append([yr, features])

    crimes_count_info[0].append(0)
    for index in range(len(crimes_count_info)):
        if index + 1 < len(crimes_count_info):
            ds: int = int(crimes_count_info[index + 1][1]) - int(
                crimes_count_info[index][1]
            )
            perc: float = round((abs(ds) / int(crimes_count_info[index][1])) * 100, 2)
            crimes_count_info[index + 1].append(perc)

    return crimes_count_info


def get_crimes_count_by_cities() -> Dict[int, Dict[int, int]]:
    sqlalchemy_session: Session = session()

    crime_counts_by_cities: Dict[int, Dict[int, int]] = {}
    now = datetime.now()
    city_codes: List[CityCodes] = sqlalchemy_session.query(CityCodes).all()

    for city_code in city_codes:
        crime_counts_dict: Dict[int, int] = {}

        for yr in range(now.year - 4, now.year + 1):
            features: int = (
                sqlalchemy_session.query(Features)
                .filter(Features.year == yr)
                .filter(Features.city_code == city_code.city_code)
                .count()
            )

            crime_counts_dict[yr] = features
        crime_counts_by_cities[city_code.city_code] = crime_counts_dict
    return crime_counts_by_cities


def get_crimes_count_by_period(
    years: Optional[List[int]] = None, periods: Optional[List[int]] = None
) -> Dict[int, Dict[int, int]]:
    now = datetime.now()
    sqlalchemy_session: Session = session()
    crimes_by_periods: Dict[int, Dict[int, int]] = {}

    if years is None and periods is None:
        years = [element for element in range(now.year - 4, now.year + 1)]
        periods = [element for element in range(1, 13)]
    elif years is None:
        years = [year for year in range(now.year - 4, now.year + 1)]
    elif periods is None:
        periods = [element for element in range(1, 13)]

    for year in years:
        years_crimes_counts_by_periods: Dict[int, int] = {}

        for period in periods:  # type: ignore
            features: int = (
                sqlalchemy_session.query(Features)
                .filter(Features.year == year)
                .filter(Features.period == period)
                .count()
            )
            logger.info(f"year: {year} | period: {period} | count: {features}")
            years_crimes_counts_by_periods[period] = features
        crimes_by_periods[year] = years_crimes_counts_by_periods

    return crimes_by_periods
