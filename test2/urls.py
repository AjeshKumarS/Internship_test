from django.urls import path

from . import views

app_name = 'test2'

urlpatterns = [
	path('', views.home, name='home'),
	path('output', views.get_output, name='output')
]
