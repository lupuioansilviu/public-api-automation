import pytest
from src.api_client import AgifyClient

client = AgifyClient()


@pytest.mark.parametrize("name", ["michael", "sarah", "andrei"])
def test_predict_age_status_200(name):
    r = client.predict_age(name)
    assert r.status_code == 200


@pytest.mark.parametrize("name", ["michael", "sarah", "andrei"])
def test_predict_age_response_shape(name):
    r = client.predict_age(name)
    data = r.json()

    assert data["name"] == name
    assert "age" in data
    assert "count" in data
    assert isinstance(data["count"], int)
    assert (data["age"] is None) or isinstance(data["age"], int)


@pytest.mark.parametrize(
    "name,country_id",
    [
        ("michael", "US"),
        ("michael", "GB"),
        ("andrei", "RO"),
    ],
)
def test_predict_age_with_country_id_has_expected_shape(name, country_id):
    r = client.predict_age(name, country_id=country_id)
    assert r.status_code == 200

    data = r.json()
    assert data["name"] == name
    assert "age" in data
    assert "count" in data


def test_predict_age_missing_name_returns_200_and_expected_keys():
    r = client.predict_age("")
    assert r.status_code == 200

    data = r.json()
    assert "name" in data
    assert "age" in data
    assert "count" in data