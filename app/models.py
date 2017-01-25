from django.db import models
from django.utils import timezone


# Create your models here.
class Employee(models.Model):
	author = models.ForeignKey('auth.User')
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	pay_per_month = models.CharField(max_length=20)
	

	def publish(self):
		self.save()

	def __str__(self):
		return "%s %s" % (self.first_name, self.last_name)

class Record(models.Model):
		Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
		#Employees = models.ManyToManyField(Employee)
		date = models.DateField(default=timezone.now)
		#month = models.IntegerField(blank=True,null=True)
		#year = models.IntegerField(blank=True,null=True)
		no_of_holidays = models.CharField(max_length=10)
		total_advance_overhead = models.CharField(max_length=15)
		no_of_hours_absent = models.CharField(max_length=10)
		no_of_ot_hours = models.CharField(max_length=10)
		key = models.AutoField(primary_key=True)

		def get_month(self):
			month = self.date.month
		
		def __str__(self):
			e = self.Employee
			return "%s %s %s - %s" % ( e.first_name,e.last_name,str(self.date.month),str(self.date.year))
			#return (str(Month.Employee))