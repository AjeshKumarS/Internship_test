from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views
from test2 import urls as test2urls
from test3 import urls as test3urls

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', views.home, name='index'),
	path('test2/', include(test2urls, namespace='test2')),
	path('test3/', include(test3urls, namespace='test3'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
