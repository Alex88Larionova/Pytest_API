import pytest
import requests

URL = "https://api.pokemonbattle.ru/v2"
TOKEN = "b99b6c3a5c0b1ea642e3507bc3efb7c5"
HEADER = {"Content-type": "application/json", "trainer_token": TOKEN}
TRAINER_ID = "21818"

"""Check status code"""


def test_status_code():
    response = requests.get(url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID})
    assert response.status_code == 200


"""Check part of response"""


def test_part_of_response():
    response_get = requests.get(
        url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID}
    )
    assert response_get.json()["data"][0]["trainer_name"] == "SashkaBukashka"


@pytest.mark.parametrize(
    "key, value",
    [("trainer_name", "SashkaBukashka"), ("id", TRAINER_ID)],
)
def test_parametrize(key, value):
    response_parametrize = requests.get(
        url=f"{URL}/trainers", params={"trainer_id": TRAINER_ID}
    )
    assert response_parametrize.json()["data"][0][key] == value
