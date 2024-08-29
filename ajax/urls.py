from django.urls import path
from . import views
urlpatterns = [
    path('search_lucky_day', views.search_lucky_day, name='search_lucky_day'),
    path('search_event_day', views.search_event_day, name='search_event_day'),
    path('event_detail', views.event_detail, name='event_detail'),
]