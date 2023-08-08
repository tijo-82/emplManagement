from pyexpat.errors import messages
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View

from employees.models import Employee
from django.template.loader import render_to_string

# Create your views here.
class employeeList(View):
    def get(self, request):
        context={}
        print("sdcjsbhdjbsdjb")
        template_name = 'employee-list.html'
        employees = Employee.objects.filter(is_deleted=False).all()
        empl=[]
        for em in employees:
            array={'first_name':em.first_name,'last_name':em.last_name,'email':em.email,'department':em.get_department_display(),'salary':em.salary}
            empl.append(array)
        context['employees']=empl
        return render(request, template_name, context)
class employeeAdd(View):
    def get(self, request):
        context={}
        template_name = 'add-employee.html'
        employees = Employee.objects.all()
        context['employees']=employees
        return render(request, template_name, context)
    def post(self, request):
        try:
            if request.method == 'POST':
                fname = request.POST['name']
                lname = request.POST['lname']
                email = request.POST['email']
                depertment = request.POST['depertment']
                salary = request.POST['salary']
                empl = Employee(first_name=fname, last_name=lname,email=email, department=depertment, salary=salary)
                empl.save()
                print(fname,"----name")
                print(depertment,"----depertment")
                print(salary,"----salary")
                return redirect(reverse('employeesApp:employee_list'))
        except Exception as e:
            messages.add_message(request, messages.WARNING, f'Failed to update profile')
            # return HttpResponseRedirect(redirect_to='/profile')

class employeeEdit(View):
    def get(self, request):
        context={}
        template_name = 'add-list.html'
        employees = Employee.objects.all()
        context['employees']=employees
        return render(request, template_name, context)
