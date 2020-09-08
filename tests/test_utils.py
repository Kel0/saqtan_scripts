import pytest

from saqtan_scripts.utils import read_json_file


@pytest.mark.parametrize("filename", (["samples/read_sample.json"]))
def test_read_json_file(helpers, filename):
    expected_data = helpers().read_json_file(filename=filename)
    data = read_json_file(filename=filename)

    assert data == expected_data
