from django.db.models import Model, TimeField, CharField, TextField, IntegerField, BooleanField, DecimalField
import requests
from bs4 import BeautifulSoup
from weather_data.models import Weather


class DailyWeather(Model):
    time = TimeField()
    temp = CharField(max_length=10)
    humidity = DecimalField()
    precip = models.CharField(max_length=20)
    conditions = models.TextField()


class HourlyWeather(Model):
    datetime = CharField(max_length = 45)
    conds = TextField()
    dewptm = DecimalField()
    fog = TextField()
    hail = TextField()
    heatindexm =
    hum =
    icon =
    metar =
    precipm =
    pressurem =
    rain = TextField(choices=["Light", "Heavy", ""])
    snow = TextField()
    tempm =
    thunder =
    tornado =
    utcdate =
    vism =
    wdird =
    wdire =
    wgustm =
    windchillm =
    wspdm =







class Date(models.Model):
    pretty = models.DateField(verbose_name=True),
    year = models.IntegerField()
    mon = models.IntegerField()
    mday = models.IntegerField()
    hour = models.IntegerField()
    min = models.IntegerField()