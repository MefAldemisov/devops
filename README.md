# Devops

The repo lists the tasks for the  devops course

## Getting Started

The goal of the first app is to show the current time in a curtain location (e.g. Moscow).
The implementation has basically two pages:
- the list of all locations
- the current time for each location


### Prerequisites

Python 3.7+

### Installing

Create a virtual environment:
```bash
$ python -m venv venv
```
Change the directory:
```bash
$ cd ./app_python
```
Install the requirements:
```bash
$ pip install -r requirements.txt
```
Run the app
```bash
$ export FLASK_APP=main
$ flask run
```
For the development mode
```bash
$ export FLASK_ENV=development
```
To export as an app:
```bash
$ export FLASK_APP=hello
```
Url to be opened:
[http://127.0.0.1:5000/time/Europe/Moscow](http://127.0.0.1:5000/time/Europe/Moscow)

### Testing

```bash
$ pip install -e .    
$ python -m pytest
```

### Linting

```bash
$ pylint app_python/*.py tests/*.py
```