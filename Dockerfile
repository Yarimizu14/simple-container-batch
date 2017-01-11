FROM python:2.7

ADD ./ /task

RUN pip install -r /task/requirements.txt

WORKDIR /task

CMD python task.py
