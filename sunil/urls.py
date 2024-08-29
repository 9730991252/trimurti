from django.urls import path
from . import views
urlpatterns = [
    path('sunil_home/', views.sunil_home, name='sunil_home'),
    ]