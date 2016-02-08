from django.db import models


# For daily production from 2008-2015:
# http://www.iso-ne.com/isoexpress/web/reports/operations/-/tree/daily-gen-fuel-type


class EnergyProduction(models.Model):
    date = models.DateField()
    coal = models.IntegerField()
    gas = models.IntegerField()
    hydro = models.IntegerField()
    nuclear = models.IntegerField()
    oil = models.IntegerField()
    refuse = models.IntegerField()
    solar = models.IntegerField()
    wind = models.IntegerField()
    total = models.IntegerField()


