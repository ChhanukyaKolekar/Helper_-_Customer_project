from django.db import models

# Create your models here.


class Helper_Info(models.Model):
    helper_id=models.CharField(max_length=10)
    name=models.CharField(max_length=120)
    gender=models.CharField(max_length=20)
    age=models.IntegerField()
    skills=models.TextField()
    status=models.CharField(max_length=100,default="AVAILABLE")

    def update_status(self):
        self.status="NOT AVAILABLE"
        self.save()

    def __str__(self):
        return self.helper_id

class Customer_Info(models.Model):
    customer_id=models.CharField(max_length=10)
    name=models.CharField(max_length=120)
    address=models.TextField()
    phone_number=models.IntegerField()
    helper_assigned=models.CharField(max_length=100, blank=True,null=True)

    def update_helper_assigned(self,hlp_id):
        self.helper_assigned=hlp_id
        self.save()
    def __str__(self):
        return self.customer_id