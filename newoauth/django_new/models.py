from django.db import models

# Create your models here.
class new_student(models.Model):
    fname=models.CharField(max_length=20)
    lname=models.CharField(max_length=20)
    age=models.IntegerField(default=0)
    address=models.CharField(max_length=30)

