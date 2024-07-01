FROM python:3.12.4-slim-bookworm

RUN apt-get update && apt-get install tzdata

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./trading_calendar /code/trading_calendar

CMD ["uvicorn", "trading_calendar.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "trading_calendar.main:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
