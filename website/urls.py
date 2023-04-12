
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('chart', views.chart,name='chart'),
    path('page', views.pageB,name='page'),
    path('log', views.log,name='log'),
    path('home', views.home,name='home'),
    path('auth', views.auth_,name='auth'),
    path('lout', views.lout,name='lout'),
    path('aboutus', views.aboutus,name='aboutus'),
]