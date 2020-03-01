# Python support can be specified down to the minor or micro version
# (e.g. 3.6 or 3.6.3).
# OS Support also exists for jessie & stretch (slim and full).
# See https://hub.docker.com/r/library/python/ for all supported Python
# tags from Docker Hub.
FROM python:3.7.2

# If you prefer miniconda:
#FROM continuumio/miniconda3
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /app/backend
ADD . /app/backend

RUN chmod g+w /app/backend

# Using pip:
RUN python3 -m pip install -r requirements.txt
CMD python3 manage.py runserver 0.0.0.0:8000

# Using pipenv:
# RUN python3 -m pip install pipenv
# COPY Pipfile ./
# COPY Pipfile.lock ./
# RUN pipenv install --system --deploy
# CMD pipenv run python3 manage.py runserver 0.0.0.0:8000


# Using miniconda (make sure to replace 'myenv' w/ your environment name):
#RUN conda env create -f environment.yml
#CMD /bin/bash -c "source activate myenv && python3 -m python scripts"
