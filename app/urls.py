from django.conf.urls import url
from . import views

urlpatterns = [url(r'^$',views.wage_list,name='wage_list'), ]