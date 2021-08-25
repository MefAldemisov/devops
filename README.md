# Devops

The repo lists the tasks for the  devops course

## Getting Started

The goal of the first app is to show the current time in a curtain location (for instance, in Moscow).
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
Run the app (from the root directory `./devops`)
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
#### Best practices of testing

##### Testable code properties
- deterministic (don't rely on the environment much, don't change over time) 
- the SRP (single responsibility principal) holds at function-level

##### Unit tests properties
- easy to write
- reliable
- readable
- fast
- not an integration test

##### Practices themselves
1. Use the IoC (Inversion of control) in case of the non-deterministic code issue


```bash
$ pip install -e .    
$ python -m pytest
```

### Linting

```bash
$ pylint app_python/*.py tests/*.py
```

### Docker

Change directory to `./app_python` to use the docker:
```bash
$ cd ./app_python
```
To build the image:
```bash
$ docker-compose up
```
To load the image from [dockerhub](https://hub.docker.com):
```bash
$ docker pull mefaldemisov/devops_lab_2:latest
$ docker run -p 5000:5000 --rm -it mefaldemisov/devops_lab_2:latest
```

