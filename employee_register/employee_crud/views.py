from django.shortcuts import render,redirect
from employee_crud.models import Employee
from employee_crud.forms import EmployeeForm
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

#Home page
def home(request):
    return redirect(request,"")

# To create employee
def emp(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showemployee")
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, "add_employee.html", {'form':form})

# To show employee details
def showemployee(request):
    employees = Employee.objects.all()
    return render(request, "showemployee.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, firstname):
    employee = Employee.objects.get(firstname=firstname)
    employee.delete()
    return redirect("/showemployee")

# To edit employee details
def editemp(request, firstname):
    employee = Employee.objects.get(firstname=firstname)
    return render(request, "edit_employee.html", {'employee':employee})

# To update employee details
def updateEmp(request, firstname):
    employee = Employee.objects.get(firstname=firstname)
    form = EmployeeForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid():  
        form.save()
        return redirect("/showemployee")
    return render(request, "edit_employee.html", {'employee': employee})


