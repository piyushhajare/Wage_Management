from django.db import models
from django.utils import timezone

# Create your models here.
class Employee(models.Model):
	author = models.ForeignKey('auth.User')
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	pay_per_month = models.CharField(max_length=20)
	created_date = models.DateTimeField(default=timezone.now)

	def publish(self):
		self.save()

	def __str__(self):
		return self.first_name

class Month(models.Model):
		date = models.DateTimeField(default=timezone.now)
		no_of_holidays = models.CharField(max_length=10)
		total_advance_overhead = models.CharField(max_length=15)


		def get_month(self):
			month = self.date.month				