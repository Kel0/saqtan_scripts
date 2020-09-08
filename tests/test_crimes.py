from unittest.mock import Mock

import pytest

from saqtan_scripts.crimes import (  # isort:skip
    get_crimes,
    handle_post_data,
    get_crime_ids,
    handle_crime_code,
)


@pytest.fixture
def mock_get_crimes_requests(mocker, helpers):
    mock_get_crimes_requests = mocker.patch("saqtan_scripts.crimes.requests.post")
    mock_get_crimes_requests.return_value.status_code = 200
    mock_get_crimes_requests.return_value.json.return_value = {
        "features": [helpers().features_item_msg()]
    }
    return mock_get_crimes_requests


@pytest.fixture
def mock_requests_json():
    mock_requests_json = Mock()
    mock_requests_json.return_value = {
        "list": [
            {
                "CRIME_ID": "336",
                "CRIME_ID_DESC": "Уклонение от призыва по мобилизации (ст.388)",
            },
            {"CRIME_ID": "NONE", "CRIME_ID_DESC": "NONE"},
        ]
    }
    return mock_requests_json


@pytest.fixture
def mock_get_crime_ids_requests(mocker, mock_requests_json):
    mock_get_crime_ids_requests = mocker.patch("saqtan_scripts.crimes.requests.get")
    mock_get_crime_ids_requests.return_value.json = mock_requests_json
    mock_get_crime_ids_requests.return_value.status_code = 200
    return mock_get_crime_ids_requests


def test_handle_post_data():
    post_data = handle_post_data(year=2020, period=1, city_code=1931)
    assert post_data == {
        "where": "YR='2020' AND PERIOD='1' AND CITY_CODE='1931'",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "*",
        "returnGeometry": "true",
        "returnTrueCurves": "false",
        "returnIdsOnly": "false",
        "returnCountOnly": "false",
        "returnZ": "false",
        "returnM": "false",
        "returnDistinctValues": "false",
        "f": "json",
    }

    post_data = handle_post_data(year=2020, city_code=1931)
    assert post_data == {
        "where": "YR='2020' AND CITY_CODE='1931'",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "*",
        "returnGeometry": "true",
        "returnTrueCurves": "false",
        "returnIdsOnly": "false",
        "returnCountOnly": "false",
        "returnZ": "false",
        "returnM": "false",
        "returnDistinctValues": "false",
        "f": "json",
    }

    post_data = handle_post_data(year=2020, period=1)
    assert post_data == {
        "where": "YR='2020' AND PERIOD='1'",
        "geometryType": "esriGeometryEnvelope",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": "*",
        "returnGeometry": "true",
        "returnTrueCurves": "false",
        "returnIdsOnly": "false",
        "returnCountOnly": "false",
        "returnZ": "false",
        "returnM": "false",
        "returnDistinctValues": "false",
        "f": "json",
    }


def test_get_crimes(helpers, mock_get_crimes_requests):
    data = get_crimes(year=2020, period=1, city_code=1931)
    assert data == helpers().get_crimes_return_msg()


def test_handle_crime_code(helpers):
    fetched_row_sample = helpers().read_json_file(
        filename="samples/api_data_crime_ids.json"
    )
    crime_code = handle_crime_code(
        crime_code=fetched_row_sample["matched_crime_codes_1"],
        fetched_row={
            "CRIME_ID": fetched_row_sample["CRIME_ID_1"],
            "CRIME_ID_DESC": fetched_row_sample["CRIME_ID_DESC_1"],
        },
    )
    assert crime_code == {
        "stat": "336",
        "crime_desc": "Уклонение от призыва по мобилизации (ст.388)",
    }

    crime_code = handle_crime_code(
        crime_code=fetched_row_sample["matched_crime_codes_2"],
        fetched_row={
            "CRIME_ID": fetched_row_sample["CRIME_ID_2"],
            "CRIME_ID_DESC": fetched_row_sample["CRIME_ID_DESC_2"],
        },
    )
    assert crime_code == {
        "stat": "3",
        "crime_desc": "Преступления против конституционных и иных прав и свобод человека и гражданина (гл. 3 УК РК)",
    }

    crime_code = handle_crime_code(
        crime_code=[],
        fetched_row={
            "CRIME_ID": fetched_row_sample["CRIME_ID_2"],
            "CRIME_ID_DESC": fetched_row_sample["CRIME_ID_DESC_2"],
        },
    )
    assert crime_code is None


def test_get_crime_ids(mock_get_crime_ids_requests):
    data = get_crime_ids()
    assert data == [
        {"stat": "388", "crime_desc": "Уклонение от призыва по мобилизации (ст.388)"}
    ]
