from django import forms
from employee_crud.models import Employee


# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"



#class loginForm(forms.ModelForm):
    #class Meta:
        #model = Login
        #fields = "__all__"