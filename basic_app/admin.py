from django.contrib import admin
from .models import *
# Register your models here.

class SchoolAdmin(admin.ModelAdmin):
	list_diplay=['name','principal','location',]

class StudentAdmin(admin.ModelAdmin):
	list_diplay=['name','age','school',]

admin.site.register(School,SchoolAdmin)
admin.site.register(Student,StudentAdmin)