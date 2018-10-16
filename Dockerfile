FROM python:3

WORKDIR /home/app

ADD . /home/app
ADD ./.pypirc ~/
RUN cp /home/app/.pypirc ~

CMD  python3 setup.py sdist bdist upload
