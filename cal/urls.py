from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
]