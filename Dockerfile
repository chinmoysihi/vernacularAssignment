FROM python:3.6-alpine

ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /vernaApp

# Set the working directory to /music_service
WORKDIR /vernaApp

COPY ./requirements.txt /vernaApp/requirements.txt

RUN pip install -r requirements.txt

COPY . /vernaApp

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



