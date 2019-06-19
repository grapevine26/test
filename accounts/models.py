from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20, null=False, verbose_name='Phone number')
    employee_id = models.CharField(max_length=20, null=False, verbose_name='Employee ID')
    department = models.CharField(max_length=100, null=False, verbose_name='Department')
    employment_date = models.DateField(null=True, verbose_name='Date of employment')
    work_status = models.PositiveIntegerField(default=True, null=False)
    usage = models.PositiveIntegerField(default=0, null=False)
