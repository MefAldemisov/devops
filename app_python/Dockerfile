FROM python:3.9-alpine
MAINTAINER MefAldemisov, alinnemef@gmail.com
# requirements.txt includes the libraries for linting and testing
# which are not nececcary for app execution
RUN pip install --no-cache-dir Flask==2.0.1 pytz==2021.1
# the `templates` directory may be potentially large
VOLUME ./templates ./templates
# the COPY is made the some directory to prevent mess in the container
COPY . /app
WORKDIR /app

EXPOSE 5000
ENV FLASK_APP=__init__.py
CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]