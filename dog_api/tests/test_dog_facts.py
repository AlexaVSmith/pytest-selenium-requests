from typing import Literal
import requests
import pytest

ENDPOINT = "https://dog.ceo/api/breeds/list/all"


def test_status_code():
    list_all = requests.get(ENDPOINT)
    assert list_all.status_code == 200


def test_status():
    list_all = requests.get(ENDPOINT).json()
    status = list_all["status"]
    assert status == "success"


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("content-type", "application/json"),
        ("content-length", "1035"),
        ("Content-Encoding", "gzip"),
    ],
)
def test_header(
    test_input: (
        Literal["content-type"]
        | Literal["content-length"]
        | Literal["Content-Encoding"]
    ),
    expected: Literal["application/json"] | Literal["1035"] | Literal["gzip"],
):
    list_all = requests.get(ENDPOINT)
    assert list_all.headers[test_input] == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        (
            "australian",
            ["kelpie", "shepherd"],
        ),
        (
            "hound",
            ["afghan", "basset", "blood", "english", "ibizan", "plott", "walker"],
        ),
        ("poodle", ["medium", "miniature", "standard", "toy"]),
    ],
)
def test_message(
    test_input: Literal["australian"] | Literal["hound"] | Literal["poodle"],
    expected: list[str],
):
    list_all = requests.get(ENDPOINT).json()
    message = list_all["message"]
    assert message[test_input] == expected
