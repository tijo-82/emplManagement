from django.db import models

# Create your models here.

class Employee(models.Model):
    DEPARTMENT = (
        (1, 'HR'),
        (2, 'DEVELOPMENT'),
        (3, 'BUSSINESS'),
        (4, 'TESTING'),
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=254, null=True, blank=True)
    department = models.PositiveSmallIntegerField(choices=DEPARTMENT, default=1, null=True, blank=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True, blank=True,auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True,auto_now=True)

    class Meta:
        db_table = 'employees'
