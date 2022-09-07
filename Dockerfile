# syntax=docker/dockerfile:1
#FROM python:3

#RUN pip install --upgrade pip

#RUN adduser -D myuser
#USER myuser
#WORKDIR /home/myuser



#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1
#WORKDIR /code
#COPY --chown=myuser:myuser requirements.txt /code/
#RUN pip install --user -r requirements.txt --root-user-action=ignore

#ENV PATH="/home/myuser/.local/bin:${PATH}"

#COPY --chown=myuser:myuser . /code/

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3.8.3-alpine



RUN useradd -D myuser
USER myuser
RUN pip install --upgrade pip

WORKDIR /home/myuser

COPY --chown=myuser:myuser requirements.txt requirements.txt
RUN pip install --user -r requirements.txt

ENV PATH="/home/user/.local/bin:${PATH}"

COPY --chown=myuser:myuser . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]