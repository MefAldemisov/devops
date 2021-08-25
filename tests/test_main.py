"""
This module is responsible for the actual testing of the app
"""
from time import sleep
from datetime import datetime

from app_python.main import get_time


def test_get_time_static():
    """
    Test for `main.get_time()` function, checks for the specified date
    """
    time_to_set = {
        "hours": 12,
        "minutes": 0,
        "seconds": 0
    }

    def time_setter(time_string: str) -> str:
        return time_string.format(*time_to_set.values())

    time_sting, expected_moscow_time = map(time_setter,
                                           ["2000-01-01 {0:0=2d}:{0:0=2d}:{0:0=2d}",
                                            "{0:0=2d} hours {0:0=2d} minutes {0:0=2d} seconds"])

    datetime_obj = datetime.strptime(time_sting, "%Y-%m-%d %H:%M:%S")
    datetime_obj_function = lambda: datetime_obj

    moscow_time = get_time("Europe/Moscow", datetime_obj_function)
    vladivostok_time = get_time("Asia/Vladivostok", datetime_obj_function)
    kirov_time = get_time("Europe/Kirov", datetime_obj_function)

    assert moscow_time != vladivostok_time, "the timezone was not applied"
    assert moscow_time == kirov_time
    assert moscow_time == expected_moscow_time, \
        "The time was set invalidly.Expected {}, got {}".format(expected_moscow_time, moscow_time)


def test_get_time_update():
    """
    Test for `main.get_time()` function, check if the time updates
    """
    moscow_time_start = get_time("Europe/Moscow")
    sleep(1)
    moscow_time_update = get_time("Europe/Moscow")
    assert moscow_time_start != moscow_time_update


def test_get_time_at(client):
    """
    Test for `main.get_time_at` function
    :param client: client for a Flask app
    """
    response = client.get("/time/Europe/Moscow")
    data = response.data.decode("utf-8")
    assert "Moscow" in data
    assert "Europe" not in data
    assert "Return" in data


def test_404(client):
    """
    Test for `main.page_not_found` and `main.get_time_at` functions.
    The goal of the check is the validation of the 404 error.
    :param client: client for a Flask app
    """
    not_found = client.get("/time/Eurape/Moscow")
    assert not_found.status_code == 404
    print("NF", not_found.data)
    assert "time zone not found" in not_found.data.decode("utf-8")
    response = client.get("/Moscow")
    assert response.status_code == 404


def test_index(client):
    """
    Test for `main.get_list_of_time_zones`
    :param client: client for a Flask app
    """
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "Europe/Moscow" in data
    assert "Asia/Vladivostok" in data
