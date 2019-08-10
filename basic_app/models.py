from django.db import models
from django.urls import reverse
# Create your models here.

class School(models.Model):
	name=models.CharField(max_length=100)
	principal=models.CharField(max_length=50)
	location=models.CharField(max_length=150)

	def __str__(self):
		return self.name



class Student(models.Model):
	name=models.CharField(max_length=30)
	age=models.PositiveIntegerField()
	school=models.ForeignKey(School,related_name='students',on_delete=models.CASCADE)

	def __str__(self):
		return self.name