"""
This module is responsible for the logic of the app
"""
from datetime import datetime
from typing import Callable

import pytz
from flask import Blueprint, render_template, abort


blueprint = Blueprint("time", __name__)
PATH_TO_COUNTER = "./data/visits.txt"

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

def update_counter():
    """
    Reads, updates and saves the visits counter
    """
    counter = get_counter() + 1
    with open(PATH_TO_COUNTER, "w") as file:
        file.write(str(counter))

def decrease_counter():
    """
    Reads, updates and saves the visits counter. This method is used for all non-root paths
    """
    counter = get_counter() - 1
    with open(PATH_TO_COUNTER, "w") as file:
        file.write(str(counter))

def get_counter() -> int:
    """
    Reads and returns the value of visits counter
    """
    with open(PATH_TO_COUNTER, "r") as file:
        counter = int(file.read())
    return counter

@blueprint.route("/", methods=["GET"])
def get_list_of_time_zones():
    """
    Renders the `index.html` with a list of possible timezones
    :return: the rendered `index.html`
    """
    update_counter()
    return render_template("index.html", list=pytz.all_timezones)

@blueprint.route("/visits", methods=["GET"])
def get_visits_page():
    """
    Renders the `visits.html` with a list of possible timezones
    :return: the rendered `visits.html`
    """
    decrease_counter()
    counter = get_counter()
    return render_template("visits.html", counter=counter)

@blueprint.route("/time/<path:zone>", methods=["GET"])
def get_time_at(zone):
    """
    Renders `time.html` with a current time in the specified timezone
    :param zone: string, the time zone
    :return: the rendered `time.html` or aborts to 404 error
    """
    decrease_counter()
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
