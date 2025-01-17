from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('get-chart-data/', get_chart_data, name='get-chart-data'),
    path('get-top-products-data/', get_top_products_data, name='get-top-products-data'),
    path('settings/', settings_page, name='settings'),
]