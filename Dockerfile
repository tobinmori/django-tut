# syntax=docker/dockerfile:1
FROM python:3.9-slim-bullseye
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore
ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#WORKDIR /code
COPY requirements.txt .
RUN pip install --root-user-action=ignore -r requirements.txt
#COPY . /code/
