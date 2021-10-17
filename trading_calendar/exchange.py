class Exchange:
    def __init__(self, mic, name, acronym, url, city, country, country_code, flag, region, calendar):
        self.mic = mic
        self.name = name
        self.acronym = acronym
        self.url = url
        self.city = city
        self.country = country
        self.country_code = country_code
        self.flag = flag
        self.region = region
        self.calendar = calendar

    def get_mic(self):
        return self.mic
    
    def get_name(self):
        return self.name

    def get_acronym(self):
        return self.acronym

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

    def get_calendar(self):
        return self.calendar