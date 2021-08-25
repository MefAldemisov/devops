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
The `requirements.txt` was generated using the following command:
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

### Unit Tests

#### Best practices of testing

##### Testable code properties

- deterministic (don't rely on the environment much, don't change over time) 
- the SRP (single responsibility principal) holds at function-level
- small coupling
- ideally, the function for testing should be [pure](https://en.wikipedia.org/wiki/Pure_function)

##### Unit tests properties

- easy to write
- reliable
- readable
- fast
- not an integration test

##### Practices themselves

1. Use the IoC (Inversion of control) in case of the non-deterministic code issue
2. Use the framework for unit testing to make it automatized
3. One assert per test ([from](https://stackify.com/unit-testing-basics-best-practices/))
4. Tests should be fast, simple and readable
5. Test should not duplicate the logic of the source code
6. Testing should be automated

To run the tests:
```bash
$ pip install -e .    
$ python -m pytest
```
To check the test coverage:
```bash
$ coverage run -m pytest
$ coverage report
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

References:
- [Flask doccumentation](https://flask.palletsprojects.com/en/2.0.x/)
- [Docker best practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/) 
- [Top 20 Dockerfile best practices](https://sysdig.com/blog/dockerfile-best-practices/)
- [Unit Tests, How to Write Testable Code and Why it Matters](https://www.toptal.com/qa/how-to-write-testable-code-and-why-it-matters)
- [Unit Testing Best Practices: 9 to Ensure You Do It Right](https://www.testim.io/blog/unit-testing-best-practices/)