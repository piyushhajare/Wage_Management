from django.shortcuts import render,HttpResponse
from .models import Employee
from .models import Month
import datetime
import calendar

def wage_list(request):
	return render(request,'app/wage_list.html',{})

def get_data(request):
	employees = Employee.objects.all()

	# To find no of working days
	full_date = datetime.datetime.now()
	no_of_sundays = sum( [ 1 for i in calendar.monthcalendar( full_date.year, full_date.month ) if i[6]!=0 ] ) 
	no_of_saturdays = sum( [ 1 for i in calendar.monthcalendar( full_date.year, full_date.month ) if i[5]!=0 ] ) 
	tupl = calendar.monthrange(full_date.year,full_date.month)
	total_days_in_month = int(tupl[1])
	total_working_days = int(total_days_in_month - ( no_of_sundays + no_of_saturdays))
	# End to find no of working days

	# To find net payable slary 
	no_of_employees = employees.count() 
	salary_payable=[]
	salary=[]
	net_payable = []
	esi = 1.75
	i=0

	while i<no_of_employees:
		salary.append( int(employees[i].pay_per_month) ) # Salary per month
		salary_payable.append( (int(employees[i].pay_per_month)/total_days_in_month) * total_working_days ) 
		net_salary = salary_payable[i] - salary_payable[i]*0.0175
		net_payable.append(net_salary)
		i+=1
	# End to find net payable slary 




	return render(request,'app/wage_list.html',{'employees':employees,'twd':total_working_days,'no_of_employees':no_of_employees,'salary':salary,
		'salary_payable':salary_payable,'net_payable':net_payable})
