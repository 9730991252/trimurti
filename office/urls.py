from django.urls import path
from . import views
urlpatterns = [
    path('office_dashboard/', views.office_dashboard, name='office_dashboard'),
    path('lucky_day/', views.lucky_day, name='lucky_day'),
    path('event/', views.event, name='event'),
    path('indraprastha/', views.indraprastha, name='indraprastha'),
    path('netaji/', views.netaji, name='netaji'),
    path('gulmohar/', views.gulmohar, name='gulmohar'),
    path('office_profile/', views.office_profile, name='office_profile'),

    ]