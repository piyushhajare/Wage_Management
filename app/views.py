from django.shortcuts import render
from .models import Employee
from .models import Month

def wage_list(request):
	return render(request,'app/wage_list.html',{})

# Create your views here.
wage_list