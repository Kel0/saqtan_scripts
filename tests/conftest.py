import json
from typing import Dict, List, Union

import pytest
from pandas import read_csv


class Helpers:
    def read_json_file(self, filename: str) -> dict:
        with open(filename, "r") as f:
            data: dict = json.load(f)
        return data

    def features_item_msg(self) -> Dict[str, Dict[str, Union[str, int, float]]]:
        return {
            "attributes": {
                "OBJECTID": 8900933,
                "ID": 0,
                "YR": 2020,
                "PERIOD": 2,
                "CRIME_CODE": "1880",
                "TIME_PERIOD": 3,
                "HARD_CODE": "3",
                "UD": "203112030001555",
                "ORGAN": "г.Тараз МВД Железнодорожный район (ОП-3)",
                "DAT_VOZB": 1581165528000,
                "DAT_SOVER": 1581193800000,
                "STAT": "ст.188 ч.3",
                "DAT_VOZB_STR": "08.02.2020",
                "DAT_SOVER_STR": "08.02.2020 20:30",
                "TZ1ID": "0000000000000200006889901",
                "REG_CODE": "193112",
                "CITY_CODE": "1931",
                "STATUS": 0,
                "ORG_CODE": "19311203",
                "ENTRYDATE": 1585699200000,
                "FZ1R18P5": "ВИШНЕВАЯ",
                "FZ1R18P6": "3",
                "TRANSGRESSION": "5",
                "ORGAN_KZ": "Жамбыл облысының ІІД Тараз қаласының ІІД №3 ПБ",
                "ORGAN_EN": "g.Taraz MVD ZHeleznodorozhny'j rajon (OP-3)",
                "FE1R29P1_ID": "039",
                "FE1R32P1": "Иные",
            },
            "geometry": {"x": 687592.9563999996, "y": 4743963.6819},
        }

    def get_crimes_return_msg(
        self,
    ) -> Dict[str, List[Dict[str, Union[str, int, float]]]]:
        return {
            "attrs": [
                {
                    "OBJECTID": 8900933,
                    "ID": 0,
                    "YR": 2020,
                    "PERIOD": 2,
                    "CRIME_CODE": "1880",
                    "TIME_PERIOD": 3,
                    "HARD_CODE": "3",
                    "UD": "203112030001555",
                    "ORGAN": "г.Тараз МВД Железнодорожный район (ОП-3)",
                    "DAT_VOZB": 1581165528000,
                    "DAT_SOVER": 1581193800000,
                    "STAT": "ст.188 ч.3",
                    "DAT_VOZB_STR": "08.02.2020",
                    "DAT_SOVER_STR": "08.02.2020 20:30",
                    "TZ1ID": "0000000000000200006889901",
                    "REG_CODE": "193112",
                    "CITY_CODE": "1931",
                    "STATUS": 0,
                    "ORG_CODE": "19311203",
                    "ENTRYDATE": 1585699200000,
                    "FZ1R18P5": "ВИШНЕВАЯ",
                    "FZ1R18P6": "3",
                    "TRANSGRESSION": "5",
                    "ORGAN_KZ": "Жамбыл облысының ІІД Тараз қаласының ІІД №3 ПБ",
                    "ORGAN_EN": "g.Taraz MVD ZHeleznodorozhny'j rajon (OP-3)",
                    "FE1R29P1_ID": "039",
                    "FE1R32P1": "Иные",
                    "x": 687592.9563999996,
                    "y": 4743963.6819,
                }
            ]
        }

    def get_crimes_counts_types_msg(self) -> List[Dict[str, Union[str, int]]]:
        return [
            {
                "year": 2020,
                "crime_code": 105,
                "crime_desc": "Доведение до самоубийства",
                "crime_count": 1032,
            },
            {
                "year": 2020,
                "crime_code": 106,
                "crime_desc": "Умышленное причинение тяжкого вреда здоровью",
                "crime_count": 1336,
            },
        ]

    def get_pd_features(self, filename: str):
        return read_csv(filename)

    def crimes_count_msg(self) -> List[List[Union[int, float]]]:
        return [
            [2016, 301056, 0],
            [2017, 284688, 5.44],
            [2018, 257269, 9.63],
            [2019, 209915, 18.41],
            [2020, 88534, 57.82],
        ]

    def crimes_count_by_cities_msg(self):
        return {1931: {2016: 20, 2017: 20, 2018: 20, 2019: 20, 2020: 20}}

    def crimes_count_by_period_msg(self):
        return {
            2016: {
                1: 20,
                2: 20,
                3: 20,
                4: 20,
                5: 20,
                6: 20,
                7: 20,
                8: 20,
                9: 20,
                10: 20,
                11: 20,
                12: 20,
            },
            2017: {
                1: 20,
                2: 20,
                3: 20,
                4: 20,
                5: 20,
                6: 20,
                7: 20,
                8: 20,
                9: 20,
                10: 20,
                11: 20,
                12: 20,
            },
            2018: {
                1: 20,
                2: 20,
                3: 20,
                4: 20,
                5: 20,
                6: 20,
                7: 20,
                8: 20,
                9: 20,
                10: 20,
                11: 20,
                12: 20,
            },
            2019: {
                1: 20,
                2: 20,
                3: 20,
                4: 20,
                5: 20,
                6: 20,
                7: 20,
                8: 20,
                9: 20,
                10: 20,
                11: 20,
                12: 20,
            },
            2020: {
                1: 20,
                2: 20,
                3: 20,
                4: 20,
                5: 20,
                6: 20,
                7: 20,
                8: 20,
                9: 20,
                10: 20,
                11: 20,
                12: 20,
            },
        }

    def crimes_count_by_periods_1case(self):
        return {
            2020: {
                1: 20,
                2: 20,
                3: 20,
                4: 20,
                5: 20,
                6: 20,
                7: 20,
                8: 20,
                9: 20,
                10: 20,
                11: 20,
                12: 20,
            }
        }

    def crimes_count_by_periods_2case(self):
        return {
            2016: {1: 20},
            2017: {1: 20},
            2018: {1: 20},
            2019: {1: 20},
            2020: {1: 20},
        }


@pytest.fixture
def helpers():
    return Helpers
