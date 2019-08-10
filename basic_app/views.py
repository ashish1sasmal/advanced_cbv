from django.shortcuts import render
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
# Create your views here.

from .import models

class IndexView(TemplateView):
	template_name='basic_app/index.html'

class SchoolListView(ListView):
	context_object_name='schools'
	model=models.School #school_list
	template_name='basic_app/school.html'

class SchoolDetailView(DetailView):
	context_object_name='details'
	model=models.School
	template_name='basic_app/school_detail.html'
