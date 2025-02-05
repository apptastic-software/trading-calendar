class Exchange:
    def __init__(self, mic, name, acronym, lei, url, city, country, country_code, flag, region, dst_transitions, currency_name, currency_code, currency_symbol, calendar):
        self.mic = mic
        self.name = name
        self.acronym = acronym
        self.lei = lei
        self.url = url
        self.city = city
        self.country = country
        self.country_code = country_code
        self.flag = flag
        self.region = region
        self.dst_transitions = dst_transitions
        self.currency_name = currency_name
        self.currency_code = currency_code
        self.currency_symbol = currency_symbol
        self.calendar = calendar

    def get_mic(self):
        return self.mic

    def get_name(self):
        return self.name

    def get_acronym(self):
        return self.acronym

    def get_lei(self):
        return self.lei

    def get_url(self):
        return self.url

    def get_city(self):
        return self.city

    def get_country(self):
        return self.country

    def get_country_code(self):
        return self.country_code

    def get_flag(self):
        return self.flag

    def get_region(self):
        return self.region

    def has_dst_transitions(self):
        return self.dst_transitions

    def get_currency_name(self):
        return self.currency_name

    def get_currency_code(self):
        return self.currency_code

    def get_currency_symbol(self):
        return self.currency_symbol

    def get_calendar(self):
        return self.calendar
