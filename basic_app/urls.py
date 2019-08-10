
from django.urls import path
from . import views
from django.conf.urls import url
from django.urls import re_path
app_name='basic_app'

urlpatterns = [

	path('',views.SchoolListView.as_view(),name='list'),
	#r'^(?P<pk>[-\w]+)/$'
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='details'),
    path('create/',views.SchoolCreateView.as_view(),name='create'),
    re_path(r'^update/(?P<pk>\d+)/$',views.SchoolUpdateView.as_view(),name='update'),

]