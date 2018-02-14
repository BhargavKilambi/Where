from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    # path(r'^$',views.home),
    url(r'home/$',views.show_places,name='places'),
    url(r'register/$',views.register,name='registration'),
    url(r'login/$',login, {'template_name': 'home/login.html'}),
    url(r'logout/$',logout, {'template_name': 'home/home.html'}),
    url(r'result/$',views.search,name='result'),
    url(r'about/$',views.about,name='about'),
    url(r'catalog/$',views.editit,name='catalog'),
    url(r'profile/$',views.myProfile,name='profile'),
    url(r'catalog/edit_profile$',views.editit,name='edit_profile'),
    url(r'profile/add_good$',views.addgoods,name='add_good'),


]
