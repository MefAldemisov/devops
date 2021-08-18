import pytz
from flask import Flask, render_template, abort
from datetime import datetime


app = Flask(__name__)


def get_time(zone: str) -> str:
	tz = pytz.timezone(zone)  # get timezone object
	time = datetime.now(tz)	  # get the current time in timezone
	return time.strftime("%H hours %M minutes %S seconds")


@app.route("/", methods=["GET"])
def get_list_of_time_zones():
	return render_template("index.html", list=pytz.all_timezones)


@app.route("/time/<path:zone>", methods=["GET"])
def get_time_at(zone):
	if zone not in pytz.all_timezones:
		abort(404)
	time = get_time(zone)
	return render_template("time.html", time=time, place=zone.split("/")[-1])


@app.errorhandler(404)
def page_not_found(_):
	return render_template("404.html"), 404
