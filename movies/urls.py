from django.urls import path
from . import views

app_name='movies'
urlpatterns = [
    path('', views.index, name='index'), 
    path('response', views.response, name='response'),
    path('response2', views.response2, name='response2'),
]