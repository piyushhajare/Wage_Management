from django.shortcuts import render,HttpResponse
from .models import Employee
from .models import Record
import datetime
import calendar

def wage_list(request):
	return render(request,'app/wage_list.html',{})

def get_data(request):
	
	date_from_user = str(request.POST.get('datepicker'))
	date_from_user = date_from_user.split(' ')# 1st month 2nd is year
	print(date_from_user)

	filtered_record = Record.objects.filter(date__year=date_from_user[1],date__month=date_from_user[0])
	employees = Employee.objects.all()
	e = Employee.objects.all()

	# To find no of working days
	full_date = datetime.datetime.now()
	no_of_sundays = sum( [ 1 for i in calendar.monthcalendar( full_date.year, full_date.month ) if i[6]!=0 ] ) 
	no_of_saturdays = sum( [ 1 for i in calendar.monthcalendar( full_date.year, full_date.month ) if i[5]!=0 ] ) 

	tupl = calendar.monthrange(full_date.year,full_date.month)
	total_days_in_month = int(tupl[1])
	total_working_days = int(total_days_in_month - ( no_of_sundays + no_of_saturdays))
	# End to find no of working days

	# To find net payable slary
	no_of_employees = filtered_record.count() 
	salary_payable=[]
	salary=[]
	net_payable = []
	no_of_holiday = []
	salary_deducted = []
	net_final_payable = []
	total_ot_hrs = []
	Ot_Salary = []
	salary_per_day=[]
	days_attended = []
	esi_cutting = []
	esi = 1.75
	i=0

	while i<no_of_employees:
		salary.append( int(filtered_record[i].Employee.pay_per_month) ) # Salary per month
		salary_per_day.append((int(filtered_record[i].Employee.pay_per_month)/total_working_days))

		

		m=filtered_record[i].Employee.record_set.all()
		no_of_holiday.append(str(int(m[0].no_of_holidays) + float(float(m[0].no_of_hours_absent)/8)))
		days_attended.append(float(total_working_days) - float(no_of_holiday[i]))

		salary_payable.append( salary_per_day[i] *  days_attended[i])
		esi_cutting.append(salary_payable[i]*0.0175)
		net_salary = salary_payable[i] - salary_payable[i]*0.0175
		net_payable.append(net_salary)

		salary_deducted.append((int(m[0].no_of_holidays) + int(int(m[0].no_of_hours_absent)/8))*salary_per_day[i])
		total_ot_hrs.append(int(m[0].no_of_ot_hours))
		Ot_Salary.append((int(m[0].no_of_ot_hours)/8)*salary_per_day[i])
		net_final_payable.append(Ot_Salary[i] + net_payable[i] -salary_deducted[i] )

		# print(no_of_holiday)

		i+=1
	# End to find net payable slary 



	return render(request,'app/wage_list.html',{'employees':filtered_record,'twd':total_working_days,'no_of_employees':no_of_employees,'salary':salary,
		'salary_payable':salary_payable,'net_payable':net_payable,'no_of_holiday':no_of_holiday,'salary_deducted':salary_deducted,
		'total_ot_hrs':total_ot_hrs,'Ot_Salary':Ot_Salary,'net_final_payable':net_final_payable,'esi':esi,
		'esi_cutting':esi_cutting,'filtered_record':filtered_record})
#  Make ESI new variable

def index_data(request):
	return render(request,'app/wage_list.html',{})	