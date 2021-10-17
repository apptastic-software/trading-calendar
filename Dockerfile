FROM python:3.9  

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./trading_calendar /code/trading_calendar

CMD ["uvicorn", "trading_calendar.main:app", "--host", "0.0.0.0", "--port", "80"]

# If running behind a proxy like Nginx or Traefik add --proxy-headers
# CMD ["uvicorn", "markets:app", "--host", "0.0.0.0", "--port", "80", "--proxy-headers"]
