import os
from fastapi import FastAPI, Depends, Request, Response, Query, HTTPException
from typing import Optional, List
from enum import Enum
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel, Field
from datetime import date, time, datetime, timedelta
from zoneinfo import ZoneInfo
from .exchanges import Exchanges as Exchanges
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware
from contextlib import asynccontextmanager
from trading_calendar import __version__

def version():
    return __version__

print("Trading Calendar version: {}".format(version()))


class Weekday(str, Enum):
    MONDAY = 'Monday'
    TUESDAY = 'Tuesday'
    WEDNESDAY = 'Wednesday'
    THURSDAY = 'Thursday'
    FRIDAY = 'Friday'
    SATURDAY = 'Saturday'
    SUNDAY = 'Sunday'

exchanges = Exchanges()
available_mic = set()
all_mic_list = []
weekday_name = [Weekday.MONDAY, Weekday.TUESDAY, Weekday.WEDNESDAY, Weekday.THURSDAY, Weekday.FRIDAY, Weekday.SATURDAY, Weekday.SUNDAY]
rate_limit = "{}/minute".format(int(os.environ.get('RATE_LIMIT', 50000)))
max_days = int(os.environ.get('MAX_DAYS', 366))


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
    {
        "name": "Version",
        "description": "Get the API version.",
    },
]


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load trading calendars on startup
    exchanges.load()
    all_mic_list.clear()
    all_mic_list.extend(list(dict.fromkeys(exchanges.get_mic_list())))
    available_mic.update(exchanges.get_mic_list())
    yield
    # Clean up trading calendars on shutdown


description = """
Trading calendar REST API with holiday, late open, and early close. Over 50 unique exchange calendars for global equity and futures markets.
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
    lifespan=lifespan
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

class MarketResponse(BaseModel):
    mic: str = Field(examples=["XNYS"])
    exchange: str = Field(examples=["New York Stock Exchange"])
    acronym: Optional[str] = Field(examples=["NYSE"])
    lei: str = Field(examples=["5493000F4ZO33MV32P92"])
    url: str = Field(examples=["https://www.nyse.com/index"])
    city: str = Field(examples=["New York"])
    country: str = Field(examples=["United States"])
    country_code: str = Field(examples=["US"])
    flag: str = Field(examples=["🇺🇸"])
    currency_name: str = Field(examples=["US dollar"])
    currency_code: str = Field(examples=["USD"])
    currency_symbol: str = Field(examples=["$"])
    region: str = Field(examples=["North America"])
    timezone: str = Field(examples=["America/New_York"])
    timezone_abbr: str = Field(examples=["EDT"])
    utc_offset: str = Field(examples=["-0400"])
    dst: bool = Field(examples=[True])
    previous_dst_transition: Optional[date] = Field(examples=["2024-03-10"])
    next_dst_transition: Optional[date] = Field(examples=["2024-11-03"])
    working_days : List[Weekday] = Field(examples=[["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]])
    open_time: str = Field(examples=["09:30"])
    close_time: str = Field(examples=["16:00"])
    early_close_time: Optional[str] = Field(examples=["13:00"])

class MarketStatusResponse(BaseModel):
    mic: str = Field(examples=["XNYS"])
    day_of_week: str = Field(examples=["Wednesday"])
    is_weekend : bool = Field(examples=[False])
    is_business_day: bool = Field(examples=[True])
    status: Status = Field(examples=["Open"])
    is_early_close: Optional[bool] = Field(examples=[False])
    local_time: datetime = Field(examples=["2024-05-01T11:05:21-04:00"])
    open_time: Optional[datetime] = Field(examples=["2024-05-01T09:30:00-04:00"])
    close_time: Optional[datetime] = Field(examples=["2024-05-01T16:00:00-04:00"])
    holiday_name: Optional[str] = Field(default=None, examples=["Labor Day"])

class TradingHoursResponse(BaseModel):
    mic: str = Field(examples=["XSTO"])
    date: str = Field(examples=["2024-04-30"])
    day_of_week: str = Field(examples=["Tuesday"])
    is_early_close: bool = Field(examples=[True])
    open_time: datetime = Field(examples=["2024-04-30T09:00:00+02:00"])
    close_time: datetime = Field(examples=["2024-04-30T13:00:00+02:00"])
    holiday_name: Optional[str] = Field(examples=["Day Before Labour Day"])

class MarketHolidayResponse(BaseModel):
    exchange: str = Field(examples=["New York Stock Exchange"])
    flag: str = Field(examples=["🇺🇸"])
    mic: str = Field(examples=["XNYS"])
    date: str = Field(examples=["2024-11-29"])
    day_of_week: str = Field(examples=["Friday"])
    is_weekend : bool = Field(examples=[False])
    is_business_day: bool = Field(examples=[True])
    holiday_name: Optional[str] = Field(examples=["Black Friday"])
    is_early_close: Optional[bool] = Field(examples=[True])
    open_time: Optional[datetime] = Field(examples=["2024-11-29T09:30:00-05:00"])
    close_time: Optional[datetime] = Field(examples=["2024-11-29T13:00:00-05:00"])

class VersionResponse(BaseModel):
    version: str = Field(examples=[version()])


def split_unique(text, delimiter=","):
    return list(dict.fromkeys(text.split(delimiter))) # unique and preserve order


def daterange(start_date, end_date):
    for n in range(int((end_date - start_date).days+1)):
        yield start_date + timedelta(n)


def is_date_of_dst_transition(dt, zone):
    _d = datetime.combine(dt.date(), time.min).replace(tzinfo=zone)
    return _d.dst() != (_d+timedelta(1)).dst()


def previous_dst_transition(dt, zone):
    for d in range(366):
        if is_date_of_dst_transition(dt - timedelta(d), zone):
            return (dt - timedelta(d)).date()
    return None


def next_dst_transition(dt, zone):
    for d in range(1, 366):
        if is_date_of_dst_transition(dt + timedelta(d), zone):
            return (dt + timedelta(d)).date()
    return None


def get_dst_transitions(dt, zone):
    next_dst = next_dst_transition(dt, zone)
    if (next_dst):
        previous = previous_dst_transition(dt, zone)
    else:
        print(zone)
        previous = None
    return next_dst, previous 


def is_dst(dt, zone):
    if zone == ZoneInfo('Europe/Dublin'):
        return bool(dt.astimezone(ZoneInfo('Europe/London')).dst())
    
    return bool(dt.dst())


def fetch_markets(mic_list):
    dt = datetime.now()
    markets = []
    dst_transitions_by_timezone = {}

    for mic in mic_list:
        exchange = exchanges.get_exchange(mic)
        if not exchange:
            continue

        calendar = exchange.get_calendar()
        tz = calendar.get_timezone()
        loc_dt = dt.astimezone(tz)
        open_time = calendar.get_open_time(loc_dt.date()).strftime("%H:%M")
        close_time = calendar.get_close_time(loc_dt.date()).strftime("%H:%M")
        dst = is_dst(loc_dt, tz)
        dst_transitions = exchange.has_dst_transitions()
        if (dst_transitions):
            transitions = dst_transitions_by_timezone.get(loc_dt.tzname())
            if not transitions:
                next_dst_transition, previous_dst_transition = get_dst_transitions(loc_dt, tz)
                dst_transitions_by_timezone[loc_dt.tzname()] = [next_dst_transition, previous_dst_transition]
            else:
                next_dst_transition = transitions[0]
                previous_dst_transition = transitions[1]
        else:
            next_dst_transition = None
            previous_dst_transition = None

        market = {
            'mic': exchange.get_mic(),
            'exchange': exchange.get_name(),
            'acronym': exchange.get_acronym(),
            'lei': exchange.get_lei(),
            'url': exchange.get_url(),
            'city': exchange.get_city(),
            'country': exchange.get_country(),
            'country_code': exchange.get_country_code(),
            'flag': exchange.get_flag(),
            'currency_name': exchange.get_currency_name(),
            'currency_code': exchange.get_currency_code(),
            'currency_symbol': exchange.get_currency_symbol(),
            'region': exchange.get_region(),
            'timezone': str(tz),
            'timezone_abbr': loc_dt.tzname(),
            'utc_offset': loc_dt.strftime("%z"),
            'dst': dst,
            'previous_dst_transition': previous_dst_transition,
            'next_dst_transition': next_dst_transition,
            'weekdays': calendar.get_weekdays(),
            'open_time': open_time,
            'close_time': close_time,
        }

        if not exchange.get_acronym():
            del market['acronym']

        if not exchange.get_lei():
            del market['lei']

        if not market['next_dst_transition']:
            del market['next_dst_transition']

        if not market['previous_dst_transition']:
            del market['previous_dst_transition']

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
            local_time = datetime.now().astimezone(tz).replace(microsecond=0)

            (holiday_name, special_open_time, early_close_time) = calendar.get_holiday_name(local_time.date())            
            is_special_open = special_open_time != None
            is_early_close = early_close_time != None

            open_time = special_open_time if (is_special_open) else calendar.get_open_time(local_time.date())
            open_time = datetime.combine(local_time.date(), open_time, tz)
            close_time = early_close_time if (is_early_close) else calendar.get_close_time(local_time.date())
            close_time = datetime.combine(local_time.date(), close_time, tz)

            is_weekend = calendar.is_weekend(local_time)
            is_business_day = (not is_weekend) and (not holiday_name or (is_special_open or is_early_close)) 
            is_open = ((open_time < close_time and local_time >= open_time and local_time < close_time) or (open_time > close_time and (local_time >= open_time or local_time < close_time)) or (open_time == close_time)) and is_business_day
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
                is_special_open = special_open_time != None
                is_early_close = early_close_time != None
                is_business_day = is_special_open or is_early_close or holiday_name == None
                if not is_business_day:
                    continue

                tz = calendar.get_timezone()
                open_time = special_open_time if (is_special_open) else calendar.get_open_time(d)
                open_time = datetime.combine(d, open_time, tz)
                close_time = early_close_time if (is_early_close) else calendar.get_close_time(d)
                close_time = datetime.combine(d, close_time, tz)

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

                is_special_open = special_open_time != None
                is_early_close = early_close_time != None
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
                open_time = special_open_time if (is_special_open) else calendar.get_open_time(d)
                open_time = datetime.combine(d, open_time, tz)
                close_time = early_close_time if (is_early_close) else calendar.get_close_time(d)
                close_time = datetime.combine(d, close_time, tz)
                holiday['is_early_close'] = is_early_close
                if is_early_close or is_special_open:
                    holiday['open_time'] = open_time
                    holiday['close_time'] = close_time
                
                holiday_list.append(holiday)

            except Exception as e:
                print("Exception in fetch_market_holidays for {}, date {}. Message: {}".format(mic, date_str, e))
    
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


def get_markets_etag(mic):
    mic_str = mic or "all"
    mic_str = mic_str.replace(",", "")
    return "markets_" + version() + mic_str


@app.get("/api/v1/markets", response_model=List[MarketResponse], tags=['Markets'])
@limiter.limit(rate_limit)
def get_markets(request: Request,
                mic: str = Query(None, title="MIC code", description="Optional list of comma separated MIC codes for which market to show data for. All market will be included if MIC code is not specified.", example="XNYS")):
    
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
        response.headers["Cache-Control"] = "max-age=300"

    return response


@app.get("/api/v1/markets/status", response_model=List[MarketStatusResponse], tags=['Market Status'])
@limiter.limit(rate_limit)
def get_market_status(request: Request,
                      mic: str = Query(None, title="MIC code", description="Optional list of comma separated MIC codes for which market to show data for. All market will be included if MIC code is not specified.", example="XNYS")):
    
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
                      mic: str = Query(None, title="MIC code", description="Optional list of comma separated MIC codes for which market to show data for. All market will be included if MIC code is not specified.", example="XNYS"),
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


@app.get("/api/v1/version", response_model=VersionResponse, tags=['Version'])
def get_version():
    return {"version": app.version}
