from django.conf.urls import url
from . import views

# urlpatterns = [url(r'^$',views.wage_list,name='wage_list'), ]
urlpatterns = [url(r'^home/',views.get_data,name='get_data'),url(r'^$',views.index_data,name='index_data') ]