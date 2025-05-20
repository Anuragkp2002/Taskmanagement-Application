from django.contrib.auth.models import AbstractUser
from django.db import models

class Users_tb(AbstractUser):
    role = models.CharField(max_length=20)

    class Meta:
        db_table='User_tb'




class Task_tb(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    assigned_to = models.ForeignKey(Users_tb, on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=20,default="Pending")
    completionreport = models.TextField(blank=True, null=True)
    worked_hours = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        db_table='Task_tb'
