from django.urls import path
from django.conf.urls import url,include
from . import views
from django.contrib.auth.views import login,logout

urlpatterns = [
    # path(r'^$',views.home),
    url(r'home/$',views.show_places,name='places'),
    url(r'register/$',views.register,name='registration'),
    url(r'add_loc/$',views.add_loc,name='add_loc'),
    url(r'login/$',login, {'template_name': 'home/login.html'}),
    url(r'logout/$',logout, {'template_name': 'home/home.html'}),
    url(r'result/$',views.search,name='result'),
    url(r'about/$',views.about,name='about'),
    url(r'catalog/$',views.editit,name='catalog'),
    url(r'profile/$',views.myProfile,name='profile'),
    url(r'profile/edit_profile$',views.edit_profile,name='edit_profile'),
    url(r'add/$',views.addgoods,name='add_goods'),
    url(r'profile/(?P<pk>\d+)/update/$',views.addgood,name='add_good_with_pk'),
    url(r'profile/(?P<pk>\d+)/delete/$',views.delete_good,name='delete_good'),


]
