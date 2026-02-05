FROM python:3.14.3-slim-trixie

RUN apt-get update && apt-get install tzdata

## To build exchange_calendars from source uncomment below and remove from requirements.txt
#RUN apt-get update && apt-get install -y git tzdata
#WORKDIR /code
#COPY ./libs /code/libs
#RUN pip install uv
#WORKDIR /code/libs/exchange_calendars
#RUN rm -rf dist && SETUPTOOLS_SCM_PRETEND_VERSION=4.12 uv build && uv pip install --system dist/*.whl

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

RUN useradd -u 1001 tc
USER 1001

COPY ./trading_calendar /code/trading_calendar

CMD ["uvicorn", "trading_calendar.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "trading_calendar.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
