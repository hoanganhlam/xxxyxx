from django.db import models


class Stock(models.Model):
    isin = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class Histr(models.Model):
    isin = models.CharField(max_length=200, primary_key=True)
    name = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    price = models.CharField(max_length=200)


class sStock(models.Model):
    symbol = models.CharField(max_length=500)
    nct = models.CharField(max_length=500)
    completion_date = models.DateField(auto_now=False)
    phase = models.CharField(max_length=25)
    title = models.CharField(
        max_length=255, default=None, blank=True, null=True)
    area = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255)
    interventions = models.CharField(max_length=255)
    ev = models.FloatField()
    net_cash = models.FloatField()
    npv = models.FloatField()
    downside = models.FloatField()
    upside = models.FloatField()
    comment = models.TextField()


class Signup(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
