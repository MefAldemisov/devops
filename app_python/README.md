# Lab 1
## Choice of the framework

### What is framework?
A framework is a piece of software, which can be used as a base for the new software.
frameworks implement relatively low-level functionality, which simplifies the process of 
high-level functionality creation.


### Why Flask?

1. Flask framework is definitely a production-ready. 
   This fact is even mention in the official [documentation](https://flask.palletsprojects.com/en/2.0.x/foreword/#what-does-micro-mean):
   
2. Security

Flask framework takes care about the security aspects of the developments. 
For instance, it provides a [protection from  XSS attack](https://flask.palletsprojects.com/en/2.0.x/advanced_foreword/#develop-for-the-web-with-caution).

## How to execute?

### Bash
```bash
$ cd ./app_python
$ export FLASK_APP=main
$ flask run
```
### Powershell
```bash
$env:FLASK_APP = "main"
> flask run
```
Url to be opened:
[http://127.0.0.1:5000/time/Europe/Moscow](http://127.0.0.1:5000/time/Europe/Moscow)

