FROM python:3
COPY . /app
WORKDIR /app
VOLUME ./templates ./templates
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=__init__.py
CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]