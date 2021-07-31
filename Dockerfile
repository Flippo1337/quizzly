FROM python:3.9-slim-buster


# copy poetry files
# COPY poetry.lock /tmp/poetry.lock
COPY pyproject.toml poetry.lock* /tmp


WORKDIR /tmp


# update and remove cache
RUN apt-get update \
&& apt-get install -y libpq-dev \
&& apt-get install -y g++ \
&& apt-get update && ACCEPT_EULA=Y apt-get install -y unixodbc-dev \
&& apt-get install --assume-yes curl \
&& rm -rf /var/lib/apt/lists/* \
&& apt-get clean

RUN pip install poetry \
&& poetry config virtualenvs.create false --local \
&& poetry install --no-interaction --no-ansi \
&& yes | poetry cache clear . --all \
&& pip cache purge