FROM python:3
COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=__init__.py
CMD [ "flask", "run", "--host", "0.0.0.0", "--port", "5000" ]

#ENTRYPOINT FLASK_APP=__init__.py flask run --host=0.0.0.0
#CMD [ "python3", "-m" , "flask", "run", "--host", "0.0.0.0"]