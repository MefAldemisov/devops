FROM python:3.9-alpine
LABEL maintainer="alinnamef@gmail.com"

WORKDIR /app
# create user, make user the owner of the directory
RUN adduser -D app_user && chown -R app_user /app
USER app_user

# requirements.txt includes the libraries for linting and testing
# which are not nececcary for app execution
# docker-requirements.txt includes only limited number of dependencies
COPY docker-requirements.txt docker-requirements.txt
RUN pip install --no-cache-dir -r docker-requirements.txt

## the `templates` directory may be potentially large
# the volumes shouldn't be used, because the files are going to be transfered through the dockerhub
COPY . /app

EXPOSE 5000
ENV FLASK_APP=__init__.py
CMD [ "python3", "-m", "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]