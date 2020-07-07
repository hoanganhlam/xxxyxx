from __future__ import absolute_import
from django.utils.timezone import timedelta
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from django.conf import settings
from celery import Celery
import os

from django.apps import apps
from homepage.yfinance_api import *
from homepage.cal_npv import *

import concurrent.futures


# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iinvest.settings')
app = Celery('iinvest')

# Using a string here means the worker will not have to
# pickle the object when using Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))


@periodic_task(run_every=timedelta(seconds=120), name="update_ev")
def update_ev():
    sStock = apps.get_model('homepage', 'sStock')
    biostock_all = sStock.objects.all()
    for row in biostock_all:
        print(row.id)
        res = sStock.objects.get(pk=row.id)
        ev = get_EV(row.symbol)
        net_cash = get_cash(res.symbol)
        down_side = calculate_downside(ev, net_cash)
        up_side = calculate_upside(ev, res.npv)
        res.ev = ev
        res.net_cash = net_cash
        res.down_side = down_side
        res.up_side = up_side
        res.save()
