import json
import logging
import logging.config
import sys
from datetime import datetime
from typing import Dict, List, Union

from saqtan_scripts.crimes import get_crimes
from saqtan_scripts.writers import Updater, Writer

from saqtan_scripts.analyzer_functions import (  # isort:skip
    get_crime_types_count,
    get_crimes_count,
    get_crimes_count_by_cities,
    get_crimes_count_by_period,
)


def setup_logging(path: str = "logging.json") -> None:
    with open(path, "rt") as f:
        config = json.load(f)
    logging.config.dictConfig(config)


def update_crimes() -> None:
    now = datetime.now()
    writer: Writer = Writer()

    data: Dict[str, List[Dict[str, Union[str, int, float]]]] = get_crimes(
        year=now.year, period=now.month
    )
    writer.write_crimes(data)


def update_crime_counts_by_types() -> None:
    now = datetime.now()
    updater: Updater = Updater()

    data: List[Dict[str, Union[str, int]]] = get_crime_types_count(year=now.year)
    updater.update_crime_types_counts(data)


def update_crimes_count_periods() -> None:
    now = datetime.now()
    updater: Updater = Updater()

    data: Dict[int, Dict[int, int]] = get_crimes_count_by_period(years=[now.year])
    updater.update_crimes_count_by_periods(data)


def update_crimes_count() -> None:
    updater: Updater = Updater()

    data: List[List[Union[int, float]]] = get_crimes_count()
    updater.update_crime_counts(data)


def update_count_crimes_by_cities() -> None:
    updater: Updater = Updater()

    data: Dict[int, Dict[int, int]] = get_crimes_count_by_cities()
    updater.update_crimes_by_cities(data)


if __name__ == "__main__":
    setup_logging()
    logger = logging.getLogger(__name__)

    if sys.argv[1] == "crimes":
        logger.info("Running update_crimes function")
        update_crimes()
        logger.info("update_crimes end it work")

    elif sys.argv[1] == "crime_counts_by_types":
        logger.info("Running update_crime_counts_by_types function")
        update_crime_counts_by_types()
        logger.info("update_crime_counts_by_types end it work")

    elif sys.argv[1] == "crimes_count_periods":
        logger.info("Running update_crimes_count_periods function")
        update_crimes_count_periods()
        logger.info("update_crimes_count_periods end it work")

    elif sys.argv[1] == "crimes_count":
        logger.info("Running update_crimes_count function")
        update_crimes_count()
        logger.info("update_crimes_count end it work")

    elif sys.argv[1] == "count_crimes_by_cities":
        logger.info("Running update_count_crimes_by_cities function")
        update_count_crimes_by_cities()
        logger.info("update_count_crimes_by_cities end it work")

    elif sys.argv[1] == "complex":
        logger.info("Complex update of data")
        logger.info("Running update_crimes function")
        update_crimes()
        logger.info("update_crimes end it work")

        logger.info("Running update_crime_counts_by_types function")
        update_crime_counts_by_types()
        logger.info("update_crime_counts_by_types end it work")

        logger.info("Running update_crimes_count_periods function")
        update_crimes_count_periods()
        logger.info("update_crimes_count_periods end it work")

        logger.info("Running update_crimes_count function")
        update_crimes_count()
        logger.info("update_crimes_count end it work")

        logger.info("Running update_count_crimes_by_cities function")
        update_count_crimes_by_cities()
        logger.info("update_count_crimes_by_cities end it work")
