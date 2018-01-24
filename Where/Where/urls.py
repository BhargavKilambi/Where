from django.contrib import admin
from django.urls import path
from Where.views import home,login_redirect
from django.conf.urls import url,include


urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^$',home, name='home'),
    url(r'^home/',include('home.urls')),
]
