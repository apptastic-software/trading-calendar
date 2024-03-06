import os
from fastapi import FastAPI, Depends, Request, Response, Query, HTTPException
from typing import Optional, List
from enum import Enum
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel
from datetime import date, datetime, timedelta
import pytz
from .exchanges import Exchanges as Exchanges
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

def version():
    return "0.0.13"

tags_metadata = [
    {
        "name": "Markets",
        "description": "Get details about the markets available in this API.",
    },
    {
        "name": "Market Status",
        "description": "Get the current status (open or closed) of a market. It takes holidays and half-days into account but does not factor in circuit breakers or halts.",
    },
    {
        "name": "Trading Hours",
        "description": "Get trading hours. It takes half-days into account.",
    },
    {
        "name": "Market Holidays",
        "description": "Get market holidays. It takes half-days into account.",
    },
]


description = """
Market calendars with the holiday, late open and early close. Over 50+ unique exchange calendars for global equity and futures markets.
"""
limiter = Limiter(key_func=get_remote_address, headers_enabled=True, enabled='RATE_LIMIT' in os.environ)
app = FastAPI(
    title="Trading Calendar",
    description=description,
    version=version(),
    contact={
        "name": "Apptastic Software",
        "url": "https://github.com/apptastic-software/trading-calendar/issues",
        "email": "apptastic.software@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://raw.githubusercontent.com/apptastic-software/trading-calendar/main/LICENSE",
    },
    openapi_tags=tags_metadata, openapi_url="/api/v1/openapi.json",
)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(GZipMiddleware, minimum_size=500)

class Status(str, Enum):
    OPEN = 'Open'
    CLOSED = 'Closed'

class Weekday(str, Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

class MarketResponse(BaseModel):
    mic: str
    exchange: str
    acronym: Optional[str]
    url: str
    city: str
    country: str
    country_code: str
    flag: str
    region: str
    timezone: str
    timezone_abbr: str
    utc_offset: str
    working_days : List[Weekday]
    open_time: str
    close_time: str
    early_close_time: Optional[str]

class MarketStatusResponse(BaseModel):
    mic: str
    day_of_week: str
    is_weekend : bool
    is_business_day: bool
    status: Status
    is_early_close: Optional[bool]
    local_time: datetime
    open_time: Optional[datetime]
    close_time: Optional[datetime]
    holiday_name: Optional[str]

class TradingHoursResponse(BaseModel):
    mic: str
    date: str
    day_of_week: str
    is_early_close: bool
    open_time: datetime
    close_time: datetime
    holiday_name: Optional[str]

class MarketHolidayResponse(BaseModel):
    mic: str
    date: str
    day_of_week: str
    is_weekend : bool
    is_business_day: bool
    holiday_name: Optional[str]
    is_early_close: Optional[bool]
    open_time: Optional[datetime]
    close_time: Optional[datetime]


exchanges = Exchanges()
available_mic = set()
all_mic_list = []
weekday_name = [Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY, Weekday.SATURDAY, Weekday.SUNDAY]
rate_limit = "{}/minute".format(int(os.environ.get('RATE_LIMIT', 50000)))
max_days = int(os.environ.get('MAX_DAYS', 366))


def split_unique(text, delimiter=","):
    return list(dict.fromkeys(text.split(delimiter))) # unique and preserve order


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days+1)):
        yield start_date + timedelta(n)


def fetch_markets(mic_list):
    dt = datetime.now()
    markets = []

    for mic in mic_list:
        exchange = exchanges.get_exchange(mic)
        if not exchange:
            continue

        calendar = exchange.get_calendar()
        tz = calendar.get_timezone()
        loc_dt = tz.localize(dt)
        open_time = calendar.get_open_time(dt.date()).strftime("%H:%M")
        close_time = calendar.get_close_time(dt.date()).strftime("%H:%M")

        market = {
            'mic': exchange.get_mic(),
            'exchange': exchange.get_name(),
            'acronym': exchange.get_acronym(),
            'url': exchange.get_url(),
            'city': exchange.get_city(),
            'country': exchange.get_country(),
            'country_code': exchange.get_country_code(),
            'flag': exchange.get_flag(),
            'region': exchange.get_region(),
            'timezone': tz.zone,
            'timezone_abbr': loc_dt.tzname(),
            'utc_offset': loc_dt.strftime("%z"),
            'weekdays' : calendar.get_weekdays(),
            'open_time' : open_time,
            'close_time' : close_time,
        }

        if not exchange.get_acronym():
            del market['acronym']

        early_close_time = calendar.get_early_close_time(dt)
        if early_close_time:
            market['early_close_time'] = early_close_time.strftime("%H:%M")

        markets.append(market)
    
    return markets


def fetch_status(mic_list):
    status_list = []
    for mic in mic_list:
        exchange = exchanges.get_exchange(mic)
        calendar = exchange.get_calendar()

        try:
            tz = calendar.get_timezone()
            tzone = pytz.timezone(tz.zone)
            local_time = datetime.now(tzone).replace(microsecond=0)

            (holiday_name, special_open_time, early_close_time) = calendar.get_holiday_name(local_time.date())            
            is_special_open = not special_open_time == None
            is_early_close = not early_close_time == None

            open_time = special_open_time if (is_special_open) else calendar.get_open_time(local_time.date())
            open_time = tzone.localize(datetime.combine(local_time.date(), open_time))
            close_time = early_close_time if (is_early_close) else calendar.get_close_time(local_time.date())
            close_time = tzone.localize(datetime.combine(local_time.date(), close_time))

            is_weekend = calendar.is_weekend(local_time)
            is_business_day = (not is_weekend) and (not holiday_name or (is_special_open or is_early_close)) 
            is_open = local_time >= open_time and local_time < close_time and is_business_day
            status = Status.OPEN if is_open else Status.CLOSED

            status = {
                'mic' : mic,
                'day_of_week' : weekday_name[local_time.weekday()],
                'is_weekend' : is_weekend,
                'is_business_day' : is_business_day,
                'status' : status,
                'is_early_close' : is_early_close,
                'local_time' : local_time,
            }

            if is_business_day:
                status['open_time'] = open_time
                status['close_time'] = close_time

            if holiday_name and len(holiday_name) > 0:
                status['holiday_name'] = holiday_name

            status_list.append(status)

        except Exception as e:
            print("Exception in fetch_status for {}. Message: {}".format(mic, e))
            pass
    
    return status_list  


def fetch_trading_hours(mic_list, start_date, end_date):
    trading_hours_list = []
    
    for d in daterange(start_date, end_date):
        date_str = str(d.strftime("%Y-%m-%d"))

        for mic in mic_list:
            exchange = exchanges.get_exchange(mic)
            calendar = exchange.get_calendar()
            try:
                is_weekend = calendar.is_weekend(d)
                if is_weekend:
                    continue

                (holiday_name, special_open_time, early_close_time) = calendar.get_holiday_name(d)
                is_special_open = not special_open_time == None
                is_early_close = not early_close_time == None
                is_business_day = is_special_open or is_early_close or holiday_name == None
                if not is_business_day:
                    continue

                tz = calendar.get_timezone()
                tzone = pytz.timezone(tz.zone)
                open_time = special_open_time if (is_special_open) else calendar.get_open_time(d)
                open_time = tzone.localize(datetime.combine(d, open_time))
                close_time = early_close_time if (is_early_close) else calendar.get_close_time(d)
                close_time = tzone.localize(datetime.combine(d, close_time))    

                trading_hours = {
                    'mic' : mic,
                    'date' : date_str,
                    'day_of_week' :  weekday_name[d.weekday()],
                    'is_early_close' : is_early_close,
                    'open_time' : open_time,
                    'close_time' : close_time,
                }

                if holiday_name and len(holiday_name) > 0:
                    trading_hours['holiday_name'] = holiday_name

                trading_hours_list.append(trading_hours)

            except Exception as e:
                print("Exception in fetch_trading_hours for {}, date {}. Message: {}".format(mic, date_str, e))
                pass
    
    return trading_hours_list


def fetch_market_holidays(mic_list, start_date, end_date):
    holiday_list = []
    
    for d in daterange(start_date, end_date):
        date_str = str(d.strftime("%Y-%m-%d"))

        for mic in mic_list:
            exchange = exchanges.get_exchange(mic)
            calendar = exchange.get_calendar()
            try:
                (holiday_name, special_open_time, early_close_time) = calendar.get_holiday_name(d)
                if holiday_name == None:
                    continue

                is_special_open = not special_open_time == None
                is_early_close = not early_close_time == None
                is_business_day = is_special_open or is_early_close

                holiday = {
                    'exchange' : exchange.get_name(),
                    'flag' : exchange.get_flag(),
                    'mic' : mic,
                    'date' : date_str,
                    'day_of_week' :  weekday_name[d.weekday()],
                    'is_weekend' : calendar.is_weekend(d),
                    'is_business_day' : is_business_day,
                }

                if len(holiday_name) > 0:
                    holiday['holiday_name'] = holiday_name

                tz = calendar.get_timezone()
                tzone = pytz.timezone(tz.zone)
                open_time = special_open_time if (is_special_open) else calendar.get_open_time(d)
                open_time = tzone.localize(datetime.combine(d, open_time))
                close_time = early_close_time if (is_early_close) else calendar.get_close_time(d)
                close_time = tzone.localize(datetime.combine(d, close_time))
                holiday['is_early_close'] = is_early_close
                if is_early_close or is_special_open:
                    holiday['open_time'] = open_time
                    holiday['close_time'] = close_time
                
                holiday_list.append(holiday)

            except Exception as e:
                print("Exception in fetch_market_holidays for {}, date {}. Message: {}".format(mic, date_str, e))
                pass
    
    return holiday_list


def validate_request_mic(mics):
    if not mics:
        return
    
    missing_mic = []
    for mic in mics:
        if mic not in available_mic:
            missing_mic.append(mic)

    if len(missing_mic) > 0:
        raise HTTPException(status_code=422, detail=[{"loc": ["query", "mic"], "msg": "MIC codes not available: {}".format(missing_mic), "type": "value_error.str"}])


def validate_request_start_end(start, end):
    if start > end:
        raise HTTPException(status_code=422, detail=[{"loc": ["query", "start", "end"], "msg": "start date after end date", "type": "value_error.date"}])
    
    delta = end - start
    if delta.days > max_days:
        raise HTTPException(status_code=422, detail=[{"loc": ["query", "start", "end"], "msg": "Maximum {} days between start date and end date".format(max_days), "type": "value_error.date"}])


@app.on_event("startup")
def startup_event():
    exchanges.load()
    all_mic_list.extend(exchanges.get_mic_list())
    available_mic.update(exchanges.get_mic_list())


def get_markets_etag(mic):
    mic_str = mic or "all"
    mic_str = mic_str.replace(",", "")
    return "markets_" + version() + mic_str

@app.get("/api/v1/markets", response_model=List[MarketResponse] , tags=['Markets'])
@limiter.limit(rate_limit)
def get_markets(request: Request,
                mic: str = Query(None, title="MIC code", description="Specify comma separated list of MIC codes for which market to show data for.", example="XNYS")):
    
    etag = request.headers.get("if-none-match")
    current_etag = get_markets_etag(mic)
    if etag == current_etag:
        return Response("", 304, headers={"etag": current_etag})

    if mic:
        mic = split_unique(mic)
        validate_request_mic(mic)
    else:
        mic = exchanges.get_mic_list()

    markets = fetch_markets(mic)
    json_markets = jsonable_encoder(markets)
    response = JSONResponse(json_markets)

    if "etag" not in response.headers:
        response.headers["etag"] = current_etag
        response.headers["Cache-Control"] = "max-age=3600"

    return response


@app.get("/api/v1/markets/status", response_model=List[MarketStatusResponse], tags=['Market Status'])
@limiter.limit(rate_limit)
def get_market_status(request: Request,
                      mic: str = Query(None, title="MIC code", description="Specify comma separated list of MIC codes for which market to show data for.", example="XNYS")):
    
    if mic:
        mic = split_unique(mic)
        validate_request_mic(mic)
    else:
        mic = all_mic_list

    status = fetch_status(mic)
    return JSONResponse(jsonable_encoder(status))

def get_trading_hours_etag(mic, start, end):
    mic_str = mic or ""
    start_str = str(start.strftime("%Y%m%d"))
    end_str = str(end.strftime("%Y%m%d"))
    return "hours_" + version() + mic_str + start_str + end_str

@app.get("/api/v1/markets/hours", response_model=List[TradingHoursResponse], tags=['Trading Hours'])
@limiter.limit(rate_limit)
def get_trading_hours(request: Request,
                      mic: str = Query(None, title="MIC code", description="Specify comma separated list of MIC codes for which market to show data for.", example="XNYS"),
                      start: date = Query(..., title="Start date", description="Show holidays starting at this date.", example=datetime.today().strftime("%Y-%m-%d")),
                      end: date = Query(..., title="End date", description="Show holidays until this date.", example=datetime.today().strftime("%Y-%m-%d"))):

    validate_request_start_end(start, end)

    etag = request.headers.get("if-none-match")
    current_etag = get_trading_hours_etag(mic, start, end)
    if etag == current_etag:
        return Response("", 304, headers={"etag": current_etag})

    if mic:
        mic = split_unique(mic)
        validate_request_mic(mic)
    else:
        mic = all_mic_list

    holidays = fetch_trading_hours(mic, start, end)
    response = JSONResponse(jsonable_encoder(holidays))

    if "etag" not in response.headers:
        response.headers["etag"] = current_etag
        response.headers["Cache-Control"] = "max-age=3600"

    return response


def get_market_holidays_etag(mic, start, end):
    mic_str = mic or ""
    start_str = str(start.strftime("%Y%m%d"))
    end_str = str(end.strftime("%Y%m%d"))
    return "holidays_" + version() + mic_str + start_str + end_str

@app.get("/api/v1/markets/holidays", response_model=List[MarketHolidayResponse], tags=['Market Holidays'])
@limiter.limit(rate_limit)
def get_market_holidays(request: Request,
                        mic: str = Query(None, title="MIC code", description="Specify comma separated list of MIC codes for which market to show data for.", example="XNYS"),
                        start: date = Query(..., title="Start date", description="Show holidays starting at this date.", example=datetime.today().strftime("%Y-%m-%d")),
                        end: date = Query(..., title="End date", description="Show holidays until this date.", example=datetime.today().strftime("%Y-%m-%d"))):
    
    validate_request_start_end(start, end)

    etag = request.headers.get("if-none-match")
    current_etag = get_market_holidays_etag(mic, start, end)
    if etag == current_etag:
        return Response("", 304, headers={"etag": current_etag})

    if mic:
        mic = split_unique(mic)
        validate_request_mic(mic)
    else:
        mic = all_mic_list

    holidays = fetch_market_holidays(mic, start, end)
    response = JSONResponse(jsonable_encoder(jsonable_encoder(holidays)))

    if "etag" not in response.headers:
        response.headers["etag"] = current_etag
        response.headers["Cache-Control"] = "max-age=3600"

    return response
