from django.urls import path

from . import views
from homepage.views import email_list_signup

urlpatterns = [
    # path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('strategy/', views.strategy, name='strategy'),
    path('example/', views.example, name='example'),
    # path('biostock/', views.biostock, name='biostock'),
    path('chemstock', views.chemstock, name='chemstock'),
    path('team/', views.team, name='team'),
    path('contact/', views.contact, name='contact'),
    path('subscribe/', email_list_signup, name='subscribe'),

    path('', views.index, name='index'),
    path('biostock/', views.biostock, name='biostock'),
    path('biostock/import-data', views.biostock_import_data,
         name='biostock_import_data'),
    path('biostock/chart/<int:id>',
         views.biostock_chart_detail, name='biostock_chart_detail'),
]
