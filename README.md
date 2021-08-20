# Devops

The repo lists the tasks for the  devops course

## Getting Started

The goal of the first app is to show the current time in a curtain location (e.g. Moscow).
The implementation has basically two pages:
- the list of all locations
- the current time for each location


### Prerequisites

Python 3.9+

### Installing

Create a virtual environment:
```bash
$ python3 -m venv venv
$ source ./venv/bin/activate
```
Change the directory:
```bash
$ cd ./app_python
```
Install the requirements:
```bash
$ pip install -r requirements.txt
```
Generation of the requirements within venv:
```bash
$ pip freeze > requirements.txt
```
Run the app (from the root directory (`./devops`))
```bash
$ flask run
```

Url to be opened:
[http://127.0.0.1:5000/time/Europe/Moscow](http://127.0.0.1:5000/time/Europe/Moscow)

For the development mode
```bash
$ export FLASK_ENV=development
```
To export as an app:
```bash
$ export FLASK_APP=app_python
```
### Testing

```bash
$ pip install -e .    
$ python -m pytest
```

### Linting

```bash
$ pylint app_python/*.py tests/*.py
```

### Useful Docker commands
```bash
$ docker build --tag app_python .
$ docker run --name app_python -p 5000:5000 app_python
$ docker rm $(docker ps -a -q)
$ docker-compose up
```
