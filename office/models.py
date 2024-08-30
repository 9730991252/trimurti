from django.db import models

# Create your models here.
class Office_employee(models.Model):
    name = models.CharField(max_length=200)
    mobile = models.IntegerField()
    pin = models.IntegerField()
    status = models.IntegerField(default=1)
    added_date = models.DateTimeField(auto_now_add=True, null=True)

class Lucky_day(models.Model):
    office_employee = models.ForeignKey(Office_employee,on_delete=models.PROTECT,default=None,null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    lucky_day = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()
    status = models.IntegerField()



class Event(models.Model):
    office_employee = models.ForeignKey(Office_employee,on_delete=models.PROTECT,default=None,null=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True)
    party_name = models.CharField(max_length=200)
    persons_day = models.IntegerField(null=True)
    persons_night = models.IntegerField(null=True)
    location = models.CharField(max_length=500)
    event_day = models.DateField()
    month = models.IntegerField()
    year = models.IntegerField()
    status = models.IntegerField()




































































