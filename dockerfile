FROM python:3

WORKDIR /home/app

COPY . /home/app
COPY ./.pypirc ~/
RUN cp /home/app/.pypirc ~

CMD  python setup.py sdist bdist upload
