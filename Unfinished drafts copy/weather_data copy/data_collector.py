import pandas as pd
import datetime


class WeatherPull():
    @property
    def string_zipcode_list(self):
        zipcode_list = list(range(1000, 6928))
        for i in zipcode_list:
            i = "0" + str(i)
        return zipcode_list

    @property
    def dates_2014(self):
        r = pd.date_range('20140101','20141231')
        return r.format(formatter=lambda x: x.strftime('%Y%m%d'))

    def clean_daily_weather(self):


        weather2014 = pd.read_json("http://api.wunderground.com/api/5921b263421e9b22/{}/q/{}.json"
                               .format(dates_2014, string_zipcode_list))

