from django.urls import path

from . import views

app_name = 'test3'

urlpatterns = [
	path('', views.home, name='home')
]
