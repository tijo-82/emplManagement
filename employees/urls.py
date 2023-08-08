# employees/urls.py
from django.urls import path
from employees.views import *
from django.conf.urls.static import static
app_name ="employeesApp"

urlpatterns = [
path('employee-list', employeeList.as_view(), name='employee_list'),
path('add-employee', employeeAdd.as_view(), name='employee_add'),
path('edit-employee', employeeEdit.as_view(), name='employee_edit'),
]