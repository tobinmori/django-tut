# syntax=docker/dockerfile:1
FROM python:3

RUN pip install --upgrade pip

RUN adduser -D myuser
USER myuser
WORKDIR /home/myuser



ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY --chown=myuser:myuser requirements.txt /code/
RUN pip install --user -r requirements.txt --root-user-action=ignore

ENV PATH="/home/myuser/.local/bin:${PATH}"

COPY --chown=myuser:myuser . /code/

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]