from django.db import models
from django.contrib.auth.models import User
#




class UserService(models.Model):
	car_name=models.CharField(max_length=100)
	service_type=models.CharField(max_length=100)
	price=models.DecimalField(max_digits=6,decimal_places=2)
	quantity=models.IntegerField()
	uid=models.ForeignKey(User,on_delete=models.CASCADE)


