from django.db import models
from django.contrib import admin
class vehicle_DB(models.Model):
    Vehicle_No=models.CharField(primary_key=True)
    Owner=models.CharField(max_length=10)
    Vehicle_Model=models.CharField()
    Vehicle_Color=models.CharField()
    Lisence=models.CharField()
    Insurance=models.CharField()
    Mobile_No=models.IntegerField()
    Address=models.TextField()
class vehicle_DBAdmin(admin.ModelAdmin):
    list_display=["Vehicle_No","Owner","Vehicle_Model","Vehicle_Color","Lisence","Insurance","Mobile_No","Address"]