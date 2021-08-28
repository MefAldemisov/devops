"""
This module is responsible the testing of `get_time` function
"""
from time import sleep, localtime
from datetime import datetime, timedelta, timezone

from app_python.main import get_time


class FixedDatetime:
    """
    This class is used to generate datetime objects with a fixed value.
    This time is set for UTC
    """

    def __init__(self, hours: int = 12,
                 minutes: int = 0,
                 seconds: int = 0,
                 date: str = "2000-01-01"):

        self.time_string = "{} {:0=2d}:{:0=2d}:{:0=2d}".\
            format(date, hours, minutes, seconds)

    @staticmethod
    def _format_expected(hours: int, minutes: int, seconds: int):
        """
        Format the string with expected outcome
        :param hours: hours in the outcome
        :param minutes: minutes in the outcome
        :param seconds: seconds in outcome
        :return: the string in format "xx hours xx minutes xx seconds"
        """
        return "{:0=2d} hours {:0=2d} minutes {:0=2d} seconds".format(hours, minutes, seconds)

    def generate_datetime(self) -> datetime:
        """
        The generator for a set of datetime objects with the same parameters
        :return: the datetime with a given date and time at UTC format
        """
        datetime_obj = datetime.strptime(self.time_string, "%Y-%m-%d %H:%M:%S")
        local_tz_offset = localtime().tm_gmtoff
        local_tz_offset_delta = timedelta(0, local_tz_offset)
        datetime_utc = datetime_obj + local_tz_offset_delta
        # the last line updates the marker of timezone
        return datetime_utc.replace(tzinfo=timezone.utc)

    def expected_time(self) -> str:
        """
        Returns the expected outcome of the `get_time` function
        :return: string in format "{:0=2d} hours {:0=2d} minutes {:0=2d} seconds"
        """
        date_time = self.generate_datetime()
        return self._format_expected(date_time.hour, date_time.minute, date_time.second)


MOSCOW = "Europe/Moscow"
KIROV = "Europe/Kirov"
VLADIVOSTOK = "Asia/Vladivostok"


def test_get_time_expected_output():
    """
    Test for `main.get_time()` function.
    Checks if the output is the in the same format, as expected
    """
    fixed_datetime = FixedDatetime()
    utc_time = get_time("UTC", fixed_datetime.generate_datetime)
    assert utc_time == fixed_datetime.expected_time()


def test_get_time_different_tz():
    """
    Test for `main.get_time()` function.
    Checks if the output is the different for locations in different timezones
    """
    fixed_datetime = FixedDatetime()
    moscow_time = get_time(MOSCOW, fixed_datetime.generate_datetime)
    vladivostok_time = get_time(VLADIVOSTOK, fixed_datetime.generate_datetime)
    assert moscow_time != vladivostok_time, "the timezone was not applied"


def test_get_time_same_tz():
    """
    Test for `main.get_time()` function.
    Checks if the output is the same for locations in the same timezone
    """
    fixed_datetime = FixedDatetime()
    moscow_time = get_time(MOSCOW, fixed_datetime.generate_datetime)
    kirov_time = get_time(KIROV, fixed_datetime.generate_datetime)
    assert moscow_time == kirov_time


def test_get_time_update():
    """
    Test for `main.get_time()` function.
    Checks if the time updates
    """
    moscow_time_start = get_time(MOSCOW)
    sleep(1)
    moscow_time_update = get_time(MOSCOW)
    assert moscow_time_start != moscow_time_update
