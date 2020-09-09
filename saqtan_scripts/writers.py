import json
import logging
from typing import Dict, List, Union

from pymysql.err import OperationalError

from .database.db import session

from .database.models import (  # isort:skip
    CrimeCodes,
    CrimeCountsByTypes,
    CrimesCount,
    Features,
    CrimesCountPeriods,
    CountCrimesByCities,
)

logger = logging.getLogger(__name__)


CRIME_ID_CONTENT_TYPE = List[Dict[str, Union[str, int, float]]]
CRIME_TYPE = Dict[str, CRIME_ID_CONTENT_TYPE]


def reload_session(func):  # Function decorator
    def wrapper(self, *args, **kwargs):
        self._reload_session()
        return func(self, *args, **kwargs)

    return wrapper


class Writer:
    def __init__(self) -> None:
        self.sqlalchemy_session = session()

    def _reload_session(self):  # pragma: no cover
        try:
            self.sqlalchemy_session.commit()
        except OperationalError as e_info:
            logger.warning(e_info)
            self.sqlalchemy_session = session()

    @reload_session
    def write_crime_codes(self, content: CRIME_ID_CONTENT_TYPE) -> None:
        for row in content:
            try:
                self.sqlalchemy_session.add(
                    CrimeCodes(crime_code=row["stat"], crime_desc=row["crime_desc"])
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(f"Failed to add: {row} | ERROR: {e_info}")
        self.sqlalchemy_session.commit()

    @reload_session
    def write_crimes(self, content: CRIME_TYPE) -> None:
        features: List[Features] = (
            self.sqlalchemy_session.query(Features)
            .filter(Features.year == content["attrs"][0]["YR"])
            .filter(Features.period == content["attrs"][0]["PERIOD"])
            .all()
        )
        key_objects: Dict[int, Dict[str, Union[str, int, float]]] = {
            element.object_id: element for element in features
        }

        for row in content["attrs"]:
            try:
                if key_objects.get(row["OBJECTID"], None) is None:  # type: ignore
                    self.sqlalchemy_session.add(
                        Features(
                            object_id=row["OBJECTID"],
                            year=row["YR"],
                            period=row["PERIOD"],
                            crime_code=row["CRIME_CODE"],
                            time_period=row["TIME_PERIOD"],
                            hard_code=row["HARD_CODE"],
                            ud=row["UD"],
                            organ=row["ORGAN"],
                            dat_vozb=row["DAT_VOZB"],
                            dat_sover=row["DAT_SOVER"],
                            stat=row["STAT"],
                            dat_vozb_str=row["DAT_VOZB_STR"],
                            dat_sover_str=row["DAT_SOVER_STR"],
                            tz1id=row["TZ1ID"],
                            reg_code=row["REG_CODE"],
                            city_code=row["CITY_CODE"],
                            status=row["STATUS"],
                            org_code=row["ORG_CODE"],
                            entrydate=row["ENTRYDATE"],
                            fz1r18p5=row["FZ1R18P5"],
                            fz1r18p6=row["FZ1R18P6"],
                            transgression=row["TRANSGRESSION"],
                            organ_kz=row["ORGAN_KZ"],
                            organ_en=row["ORGAN_EN"],
                            fe1r29p1_id=row["FE1R29P1_ID"],
                            fe1r32p1=row["FE1R32P1"],
                            x_geo=row["x"],
                            y_geo=row["y"],
                        )
                    )
            except Exception as e_info:  # pragma: no cover
                logger.error(f"Failed to add: {row} | ERROR: {e_info}")
        self.sqlalchemy_session.commit()

    @reload_session
    def write_crime_types_counts(
        self, content: List[Dict[str, Union[str, int]]]
    ) -> None:
        for row in content:
            try:
                self.sqlalchemy_session.add(
                    CrimeCountsByTypes(
                        year=row["year"],
                        crime_code=row["crime_code"],
                        crime_type=row["crime_desc"],
                        crime_count=row["crime_count"],
                    )
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(f"Failed to add: {row} | ERROR: {e_info}")
        self.sqlalchemy_session.commit()

    @reload_session
    def write_crime_counts(self, content: List[List[Union[int, float]]]) -> None:
        for row in content:
            try:
                self.sqlalchemy_session.add(
                    CrimesCount(year=row[0], crimes_count=row[1], before_perc=row[2])
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(f"Failed to add: {row} | ERROR: {e_info}")
        self.sqlalchemy_session.commit()

    @reload_session
    def write_crime_counts_by_cities(self, content: Dict[int, Dict[int, int]]) -> None:
        for key, value in content.items():
            try:
                self.sqlalchemy_session.add(
                    CountCrimesByCities(city_code=key, json_data=json.dumps(value))
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(e_info)
        self.sqlalchemy_session.commit()

    @reload_session
    def write_crimes_count_by_periods(self, content: Dict[int, Dict[int, int]]) -> None:
        for key, value in content.items():
            try:
                self.sqlalchemy_session.add(
                    CrimesCountPeriods(year=key, json_data=json.dumps(value))
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(e_info)
        self.sqlalchemy_session.commit()


class Updater:
    def __init__(self):
        self.sqlalchemy_session = session()

    def _reload_session(self):  # pragma: no cover
        try:
            self.sqlalchemy_session.commit()
        except OperationalError as e_info:
            logger.warning(e_info)
            self.sqlalchemy_session = session()

    @reload_session
    def update_crime_types_counts(
        self, content: List[Dict[str, Union[str, int]]]
    ) -> None:
        for row in content:
            try:
                (
                    self.sqlalchemy_session.query(CrimeCountsByTypes)
                    .filter(CrimeCountsByTypes.year == row["year"])
                    .filter(CrimeCountsByTypes.crime_code == row["crime_code"])
                    .update({CrimeCountsByTypes.crime_count: row["crime_count"]})
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(f"Failed to add: {row} | ERROR: {e_info}")
        self.sqlalchemy_session.commit()

    @reload_session
    def update_crimes_by_cities(self, content: Dict[int, Dict[int, int]]) -> None:
        for key, value in content.items():
            try:
                (
                    self.sqlalchemy_session.query(CountCrimesByCities)
                    .filter(CountCrimesByCities.city_code == key)
                    .update({CountCrimesByCities.json_data: json.dumps(value)})
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(e_info)
        self.sqlalchemy_session.commit()

    @reload_session
    def update_crime_counts(self, content: List[List[Union[int, float]]]) -> None:
        for row in content:
            try:
                (
                    self.sqlalchemy_session.query(CrimesCount)
                    .filter(CrimesCount.year == row[0])
                    .update(
                        {
                            CrimesCount.crimes_count: row[1],
                            CrimesCount.before_perc: row[2],
                        }
                    )
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(f"Failed to add: {row} | ERROR: {e_info}")
        self.sqlalchemy_session.commit()

    @reload_session
    def update_crimes_count_by_periods(
        self, content: Dict[int, Dict[int, int]]
    ) -> None:
        for key, value in content.items():
            try:
                (
                    self.sqlalchemy_session.query(CrimesCountPeriods)
                    .filter(CrimesCountPeriods.year == key)
                    .update({CrimesCountPeriods.json_data: json.dumps(value)})
                )
            except Exception as e_info:  # pragma: no cover
                logger.error(e_info)
        self.sqlalchemy_session.commit()
