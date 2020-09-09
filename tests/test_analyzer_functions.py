from datetime import datetime
from unittest.mock import Mock

import pytest

from .fake_models import CityCodes, CrimeCodes

from saqtan_scripts.analyzer_functions import (  # isort:skip
    get_crime_types_count,
    get_crimes_count,
    get_crimes_count_by_cities,
    get_crimes_count_by_period,
)


@pytest.fixture
def mock_analyzer_functions_datetime(mocker):
    mock_analyzer_functions_datetime = mocker.patch(
        "saqtan_scripts.analyzer_functions.datetime"
    )
    mock_analyzer_functions_datetime.now.return_value = datetime(2020, 1, 1, 14, 0)
    return mock_analyzer_functions_datetime


@pytest.fixture
def mock_session_query_all():
    mock_session_query_all = Mock()
    mock_session_query_all.query.return_value.all.return_value = [
        CrimeCodes(id=1, crime_code=188, crime_desc="Кража"),
        CrimeCodes(id=1, crime_code=99, crime_desc="Убийство"),
    ]
    mock_session_query_all.query.return_value.filter.return_value.count.side_effect = [
        301056,
        284688,
        257269,
        209915,
        88534,
    ]
    # fmt: off
    (
        mock_session_query_all.query.return_value
        .filter.return_value.filter.return_value
        .count.return_value
    ) = 20
    # fmt: on
    return mock_session_query_all


@pytest.fixture
def mock_analyzer_functions_session(
    mocker, mock_session_query_all, mock_session_query_all_get_crimes_count_by_cities
):
    mock_analyzer_functions_session = mocker.patch(
        "saqtan_scripts.analyzer_functions.session"
    )
    mock_analyzer_functions_session.side_effect = [
        mock_session_query_all,
        mock_session_query_all_get_crimes_count_by_cities,
        mock_session_query_all,
    ]
    return mock_analyzer_functions_session


@pytest.fixture
def mock_session_query_all_get_crimes_count_by_cities():
    mock_session_query_all_get_crimes_count_by_cities = Mock()
    mock_session_query_all_get_crimes_count_by_cities.query.return_value.all.return_value = [
        CityCodes(id=1, city_code=1931, city_name="Тараз", type="city"),
    ]
    # fmt: off
    (
        mock_session_query_all_get_crimes_count_by_cities
        .query.return_value.filter.return_value.filter.return_value
        .count.return_value
    ) = 20
    # fmt: on
    return mock_session_query_all_get_crimes_count_by_cities


def test_get_crime_types_count(
    mock_analyzer_functions_session,
    mock_session_query_all,
):
    data = get_crime_types_count(year=2016)
    assert data == [
        {"year": 2016, "crime_code": 188, "crime_desc": "Кража", "crime_count": 20},
        {"year": 2016, "crime_code": 99, "crime_desc": "Убийство", "crime_count": 20},
    ]


def test_get_crimes_count(
    helpers, mock_analyzer_functions_session, mock_session_query_all
):
    data = get_crimes_count()
    assert data == helpers().crimes_count_msg()


def test_get_crimes_count_by_cities(
    helpers,
    mock_analyzer_functions_session,
    mock_session_query_all_get_crimes_count_by_cities,
    mock_analyzer_functions_datetime,
):
    mock_analyzer_functions_session()  # pass first side-effect

    data = get_crimes_count_by_cities()
    assert data == helpers().crimes_count_by_cities_msg()


def test_get_crimes_count_by_period(
    helpers,
    mock_analyzer_functions_session,
    mock_session_query_all_get_crimes_count_by_cities,
    mock_analyzer_functions_datetime,
):
    data = get_crimes_count_by_period()
    assert data == helpers().crimes_count_by_period_msg()

    data = get_crimes_count_by_period(years=[2020])
    assert data == helpers().crimes_count_by_periods_1case()

    data = get_crimes_count_by_period(periods=[1])
    assert data == helpers().crimes_count_by_periods_2case()
