from datetime import date, datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from numpy import datetime64
import pandas as pd
import holidays

print("Holidays version: {}".format(holidays.__version__))

class Calendar:
    def __init__(self, calendar, country_code):
        self.calendar = calendar
        self.regular_holidays = None
        self.adhoc_holidays = set()
        self.precomputed_holidays = set()
        self.early_close = []
        self.special_closes_adhoc = []
        self.special_opens = []
        self.special_opens_adhoc = []
        self.weekday_early_close = {}
        self.country_code = country_code        

        if calendar.regular_holidays:
            try:
                self.regular_holidays = calendar.regular_holidays.holidays(return_name=True)
            except Exception as e:
                print("Exception in regular_holidays for {}. Message: {}".format(calendar.name, e))

        for adhoc_holiday in calendar.adhoc_holidays:
            try:
                if isinstance(adhoc_holiday, str):
                    self.adhoc_holidays.add(adhoc_holiday)
                elif isinstance(adhoc_holiday, datetime64):
                    self.adhoc_holidays.add(pd.to_datetime(adhoc_holiday).strftime('%Y-%m-%d'))
                else:
                    self.adhoc_holidays.add(str(adhoc_holiday.date()))
            except Exception as e:
                print("Exception in adhoc_holidays for {}. Message: {}".format(calendar.name, e))

        if hasattr(self.calendar, 'precomputed_holidays'):
            try:
                for precomputed_holiday in calendar.precomputed_holidays():
                    if isinstance(precomputed_holiday, pd.DatetimeIndex):
                        for precomputed_date in precomputed_holiday:
                            self.precomputed_holidays.add(str(precomputed_date.date()))
                    else:
                        self.precomputed_holidays.add(str(precomputed_holiday.date()))
            except Exception as e:
                print("Exception in precomputed_holidays for {}. Message: {}".format(calendar.name, e))

        for special_close in calendar.special_closes: 
            try:
                (close_time, early_close_holidays) = special_close
                if isinstance(early_close_holidays, int):
                    self.weekday_early_close[early_close_holidays] = close_time
                else:
                    holiday = early_close_holidays.holidays(return_name=True)
                    self.early_close.append((close_time, holiday))
            except Exception as e:
                print("Exception in special_closes for {}. Message: {}".format(calendar.name, e))

        for special_closes_adhoc in calendar.special_closes_adhoc: 
            try:
                (close_time, closes) = special_closes_adhoc
                close_dates = set()
                for close in closes:
                    if isinstance(close, str):
                        close_dates.add(close)
                    elif isinstance(close, datetime64):
                        close_dates.add(pd.to_datetime(close).strftime('%Y-%m-%d'))
                    else:
                        close_dates.add(str(close.date()))            
                self.special_closes_adhoc.append((close_time, close_dates))
            except Exception as e:
                print("Exception in special_closes_adhoc for {}. Message: {}".format(calendar.name, e))

        for special_opens in calendar.special_opens: 
            try:
                (open_time, special_open) = special_opens
                holiday = special_open.holidays(return_name=True)
                self.special_opens.append((open_time, holiday))
            except Exception as e:
                print("Exception in special_opens for {}. Message: {}".format(calendar.name, e))

        for special_opens_adhoc in calendar.special_opens_adhoc:
            try:
                (open_time, opens) = special_opens_adhoc
                open_dates = set()
                for open in opens:
                    if isinstance(open, str):
                        open_dates.add(open)
                    elif isinstance(open, datetime64):
                        open_dates.add(pd.to_datetime(open).strftime('%Y-%m-%d'))
                    else:
                        open_dates.add(str(open.date()))            
                self.special_opens_adhoc.append((open_time, open_dates))
            except Exception as e:
                print("Exception in special_opens_adhoc for {}. Message: {}".format(calendar.name, e))

        self.weekdays = []
        if self.calendar.weekmask[6] == '1':
            self.weekdays.append('Sunday')
        if self.calendar.weekmask[0] == '1':
            self.weekdays.append('Monday')
        if self.calendar.weekmask[1] == '1':
            self.weekdays.append('Tuesday')
        if self.calendar.weekmask[2] == '1':
            self.weekdays.append('Wednesday')
        if self.calendar.weekmask[3] == '1':
            self.weekdays.append('Thursday')
        if self.calendar.weekmask[4] == '1':
            self.weekdays.append('Friday')
        if self.calendar.weekmask[5] == '1':
            self.weekdays.append('Saturday')

    def __get_time(self, now, times):
        for i, (datetime, time) in reversed(list(enumerate(times))):
            if datetime == None or now < datetime.date():
                return time
    
        return None
    
    def get_timezone(self):
        return self.calendar.tz

    def get_open_time(self, ts):
        return self.__get_time(ts, self.calendar.open_times)
    
    def get_close_time(self, ts):
        return self.__get_time(ts, self.calendar.close_times)

    def get_early_close_time(self, ts):
        if hasattr(self.calendar, 'regular_early_close'):
            return self.calendar.regular_early_close
        else:
            return None

    def is_session(self, ts):
        return self.calendar.is_session(ts)

    def is_weekend(self, ts):
        return self.calendar.weekmask[ts.weekday()] == '0'

    def get_weekmask(self):
        return self.calendar.weekmask

    def get_weekdays(self):
        return self.weekdays

    def get_holiday_name(self, ts):
        default_name = ''
        date_str = str(ts.strftime('%Y-%m-%d'))

        if self.regular_holidays is not None:
            try:          
                value = self.regular_holidays[date_str]
                if isinstance(value, pd.Series):
                    return (value[1], None, None)
                else:
                    return (value, None, None)
            except Exception as _:
                pass

        if date_str in self.adhoc_holidays:
            holiday_name = self.get_country_holiday_name(ts)
            holiday_name = holiday_name if holiday_name is not None else default_name
            return (holiday_name, None, None)

        if date_str in self.precomputed_holidays:
            holiday_name = self.get_country_holiday_name(ts)
            holiday_name = holiday_name if holiday_name is not None else default_name
            return (holiday_name, None, None)

        holiday_name = None
        special_open_time = None
        early_close_time = None

        for early_close in self.early_close:
            try:
                (close_time, holidays) = early_close
                holiday_name = holidays[date_str]
                early_close_time = close_time
            except Exception as _:
                pass

        if not early_close_time:
            for special_closes_adhoc in self.special_closes_adhoc:
                (close_time, close_dates) = special_closes_adhoc
                if date_str in close_dates:
                    holiday_name = default_name if not holiday_name else holiday_name
                    early_close_time = close_time

        for special_opens in self.special_opens:
            try:
                (open_time, holidays) = special_opens
                holiday_name = holidays[date_str] if not holiday_name else holiday_name
                special_open_time = open_time
            except Exception as _:
                pass

        if not special_open_time:
            for special_opens_adhoc in self.special_opens_adhoc:
                (open_time, open_dates) = special_opens_adhoc
                if date_str in open_dates:
                    holiday_name = default_name if not holiday_name else holiday_name
                    special_open_time = open_time

        if (holiday_name == default_name):
            name = self.get_country_holiday_name(ts)
            holiday_name = name if name is not None else holiday_name

        if ts.weekday() in self.weekday_early_close:
            early_close_time = self.weekday_early_close[ts.weekday()]

        return (holiday_name, special_open_time, early_close_time)

    def get_country_holiday_name(self, ts):
        date_str = str(ts.strftime('%Y-%m-%d'))

        try:
            country_holiday = holidays.utils.country_holidays(self.country_code, language='en_US')
            if country_holiday is None:
                return None

            name = country_holiday.get(date_str)
            if name is not None:
                return name

            for subdivision in country_holiday.subdivisions:
                subdivisions_holiday = holidays.utils.country_holidays(self.country_code, subdiv=subdivision, language='en_US')
                name = subdivisions_holiday.get(date_str)
                if name is not None:
                    return name
        except Exception as _:
            pass

        return None
