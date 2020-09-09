from unittest.mock import Mock

import pytest

from saqtan_scripts.writers import Updater, Writer

from .fake_models import Features


@pytest.fixture
def mock_add_commit():
    mock_add_commit = Mock()
    mock_add_commit.add.return_value = None
    mock_add_commit.commit.return_value = None
    mock_add_commit.query.return_value.filter.return_value.filter.return_value.all.return_value = [
        Features(
            id=1,
            object_id=421,
            year=2020,
            period=2,
            crime_code="1880",
            time_period=3,
            hard_code="3",
            ud="203112030001555",
            organ="organ",
            dat_vozb=1581165528000,
            dat_sover=1581165528000,
            stat="08.02.2020",
            dat_vozb_str="08.02.2020",
            dat_sover_str="08.02.2020",
            tz1id="0000000000000200006889901",
            reg_code="193112",
            city_code=1931,
            status=0,
            org_code="19311203",
            entrydate=1585699200000,
            fz1r18p5="ВИШНЕВАЯ",
            fz1r18p6="3",
            transgression="5",
            organ_kz="organkz",
            organ_en="oraganen",
            fe1r29p1_id="039",
            fe1r32p1="Иные",
            x_geo=687592.9563999996,
            y_geo=687592.9563999996,
        )
    ]
    mock_add_commit.query.return_value.filter.return_value.filter.return_value.update.return_value = (
        None
    )
    mock_add_commit.query.return_value.filter.return_value.update.return_value = None
    return mock_add_commit


@pytest.fixture
def mock_writers_session(mocker, mock_add_commit):
    mock_writers_session = mocker.patch("saqtan_scripts.writers.session")
    mock_writers_session.return_value = mock_add_commit
    return mock_writers_session


def test_write_crime_codes(mock_writers_session, mock_add_commit):
    writer = Writer()

    writer.write_crime_codes(content=[{"stat": "366", "crime_desc": "Desc"}])

    assert mock_add_commit.add.called
    assert mock_add_commit.commit.called


def test_write_crimes(helpers, mock_writers_session, mock_add_commit):
    writer = Writer()

    writer.write_crimes(content=helpers().get_crimes_return_msg())

    assert mock_add_commit.add.called
    assert mock_add_commit.commit.called


def test_write_crime_types_counts(helpers, mock_writers_session, mock_add_commit):
    writer = Writer()

    writer.write_crime_types_counts(helpers().get_crimes_counts_types_msg())

    assert mock_add_commit.add.called
    assert mock_add_commit.commit.called


def test_write_crime_counts(helpers, mock_writers_session, mock_add_commit):
    writer = Writer()

    writer.write_crime_counts(helpers().crimes_count_msg())

    assert mock_add_commit.add.called
    assert mock_add_commit.commit.called


def test_write_crime_counts_by_cities(helpers, mock_writers_session, mock_add_commit):
    writer = Writer()

    writer.write_crime_counts_by_cities(helpers().crimes_count_by_cities_msg())

    assert mock_add_commit.add.called
    assert mock_add_commit.commit.called


def test_write_crimes_count_by_periods(helpers, mock_writers_session, mock_add_commit):
    writer = Writer()

    writer.write_crimes_count_by_periods(helpers().crimes_count_by_period_msg())

    assert mock_add_commit.add.called
    assert mock_add_commit.commit.called


# --------------------Updater tests---------------------


def test_update_crime_types_counts(helpers, mock_writers_session, mock_add_commit):
    updater = Updater()

    updater.update_crime_types_counts(helpers().get_crimes_counts_types_msg())

    assert (
        mock_add_commit.query.return_value.filter.return_value.filter.return_value.update.called
    )
    assert mock_add_commit.commit.called


def test_update_crimes_by_cities(helpers, mock_writers_session, mock_add_commit):
    updater = Updater()

    updater.update_crimes_by_cities(helpers().crimes_count_by_cities_msg())

    assert mock_add_commit.query.return_value.filter.return_value.update.called
    assert mock_add_commit.commit.called


def test_update_crime_counts(helpers, mock_writers_session, mock_add_commit):
    updater = Updater()

    updater.update_crime_counts(helpers().crimes_count_msg())

    assert mock_add_commit.query.return_value.filter.return_value.update.called
    assert mock_add_commit.commit.called


def test_update_crimes_count_by_periods(helpers, mock_writers_session, mock_add_commit):
    updater = Updater()

    updater.update_crimes_count_by_periods(helpers().crimes_count_by_period_msg())

    assert mock_add_commit.query.return_value.filter.return_value.update.called
    assert mock_add_commit.commit.called
