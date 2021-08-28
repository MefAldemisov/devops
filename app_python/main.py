"""
This module is responsible for the logic of the app
"""
from datetime import datetime
from typing import Callable

import pytz
from flask import Blueprint, render_template, abort


blueprint = Blueprint("time", __name__)


def get_current_time() -> datetime:
    """
    Returns the current UTC time
    :return: the datetime object with UTC time
    """
    return datetime.now(pytz.utc)


def get_time(zone: str,
             datetime_generator: Callable[..., datetime] = get_current_time) -> str:
    """
    Gets the current time in the specified timezone
    :param zone: string from the list pytz.all_timezones
    :param datetime_generator: function, that returns the datetime object for a given time
    the default value is the current time
    :return: the string, which describes the current time in the given time zone
    """
    time_zone = pytz.timezone(zone)                         # get timezone object
    time = datetime_generator().astimezone(time_zone)	    # get the current time in timezone
    return time.strftime("%H hours %M minutes %S seconds")  # generate and return string


@blueprint.route("/", methods=["GET"])
def get_list_of_time_zones():
    """
    Renders the `index.html` with a list of possible timezones
    :return: the rendered `index.html`
    """
    return render_template("index.html", list=pytz.all_timezones)


@blueprint.route("/time/<path:zone>", methods=["GET"])
def get_time_at(zone):
    """
    Renders `time.html` with a current time in the specified timezone
    :param zone: string, the time zone
    :return: the rendered `time.html` or aborts to 404 error
    """
    if zone not in pytz.all_timezones:
        abort(404)
    time = get_time(zone)
    return render_template("time.html", time=time, place=zone.split("/")[-1])


@blueprint.errorhandler(404)
def page_not_found(_):
    """
    Renders 404 page
    :return: Rendered `404.html`
    """
    return render_template("404.html"), 404
