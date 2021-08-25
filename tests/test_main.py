"""
This module is responsible the testing of `get_time` finction
"""
from time import sleep
from datetime import datetime

from app_python.main import get_time


class FixedDatetime:
    """
    This class is used to generate datetime objects with a fixed value
    """

    def __init__(self, hours: int = 12,
                 minutes: int = 0,
                 seconds: int = 0,
                 date: str = "2000-01-01"):

        self.time_string = "{} {:0=2d}:{:0=2d}:{:0=2d}".\
            format(date, hours, minutes, seconds)

        self.expected_time = "{:0=2d} hours {:0=2d} minutes {:0=2d} seconds".\
            format(hours, minutes, seconds)

    def generate_datetime(self) -> datetime:
        """
        The generator for a set of datetime objects with the same parameters
        :return: the datetime with a given date and time
        """
        datetime_obj = datetime.strptime(self.time_string, "%Y-%m-%d %H:%M:%S")
        return datetime_obj

    def get_expected_time(self) -> str:
        """
        Returns the expected outcome of the `get_time` function
        :return: string in format "{:0=2d} hours {:0=2d} minutes {:0=2d} seconds"
        """
        return self.expected_time


def test_get_time_expected_output():
    """
    Test for `main.get_time()` function.
    Checks if the output is the in the same format, as expected
    """
    fixed_datetime = FixedDatetime()
    moscow_time = get_time("Europe/Moscow", fixed_datetime.generate_datetime)
    assert moscow_time == fixed_datetime.expected_time


def test_get_time_different_tz():
    """
    Test for `main.get_time()` function.
    Checks if the output is the different for locations in different timezones
    """
    fixed_datetime = FixedDatetime()
    moscow_time = get_time("Europe/Moscow", fixed_datetime.generate_datetime)
    vladivostok_time = get_time("Asia/Vladivostok", fixed_datetime.generate_datetime)
    assert moscow_time != vladivostok_time, "the timezone was not applied"


def test_get_time_same_tz():
    """
    Test for `main.get_time()` function.
    Checks if the output is the same for locations in the same timezone
    """
    fixed_datetime = FixedDatetime()
    moscow_time = get_time("Europe/Moscow", fixed_datetime.generate_datetime)
    kirov_time = get_time("Europe/Kirov", fixed_datetime.generate_datetime)
    assert moscow_time == kirov_time


def test_get_time_update():
    """
    Test for `main.get_time()` function.
    Checks if the time updates
    """
    moscow_time_start = get_time("Europe/Moscow")
    sleep(1)
    moscow_time_update = get_time("Europe/Moscow")
    assert moscow_time_start != moscow_time_update
