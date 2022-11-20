FROM python:3.9.13

RUN mkdir /stepByStepApiAutomation

WORKDIR /stepByStepApiAutomation

ADD . /stepByStepApiAutomation/

RUN python3 setup.py install