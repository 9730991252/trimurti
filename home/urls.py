from django.urls import path
from home import views
urlpatterns = [
    path('', views.index, name='index'),
    path('sunil_login/', views.sunil_login, name='sunil_login'),
    path('login/', views.login, name='login'),
    path('office_logout/', views.office_logout, name='office_logout'),
]