from django import forms
from .models import Employee,Record

class PostForm(forms.ModelForm):

	class Meta:
		model = Record
		fields = ('Date')
			