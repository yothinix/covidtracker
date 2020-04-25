FROM python:3.7

ENV APPLICATION_ROOT /app/
RUN mkdir $APPLICATION_ROOT
COPY . $APPLICATION_ROOT

RUN pip install -r /app/requirements/dev.txt

WORKDIR $APPLICATION_ROOT/covidtracker/
