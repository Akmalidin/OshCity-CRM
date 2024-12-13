from django.urls import path

from .views import *


urlpatterns = [
    path('<int:pk>/', index, name='index'),
    path('scanner/', scanner, name='scanner'),
    path('features/', features, name='features'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('faq/', faq, name='faq'),
    path('pricing/', pricing, name='pricing'),
    path('clients/', clients, name='clients'),

]