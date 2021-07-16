FROM python:3.9-slim-buster
# FROM python:3.10.0b4-slim-buster


# copy poetry files
# COPY poetry.lock /tmp/poetry.lock
COPY pyproject.toml poetry.lock* /tmp


WORKDIR /tmp


# update and remove cache
RUN apt-get update \
&& apt-get update \
&& apt-get install -y gettext \
&& apt-get install -y libpq-dev \
&& apt-get install -y g++ \
&& apt-get update && ACCEPT_EULA=Y apt-get install -y unixodbc-dev \
&& apt-get install --assume-yes curl \
# MSODBC
# && apt-get install -y gnupg2 \
# && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
# && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list \
#&& apt-get update \
# && ACCEPT_EULA=Y apt-get install --assume-yes msodbcsql17 \
&& rm -rf /var/lib/apt/lists/*

RUN pip install poetry \
&& poetry config virtualenvs.create false --local \
&& poetry install --no-interaction --no-ansi \
&& yes | poetry cache clear . --all \
&& pip cache purge