
from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import re_path
app_name='basic_app'

urlpatterns = [
	path('',views.IndexView.as_view(),name='home'),
	path('list/',views.SchoolListView.as_view(),name='list'),
	#r'^(?P<pk>[-\w]+)/$'
    path('list/<int:pk>/',views.SchoolDetailView.as_view(),name='details'),
]