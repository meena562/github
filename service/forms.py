from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from service.models import UserService


class UsForm(UserCreationForm):
	password1=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border-success","placeholder":"enter password"}))
	password2=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control border-success","placeholder":"confirm password"}))


	class Meta:
		model=User
		fields = ['username','email']
		widgets = {
		"username":forms.TextInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter Username",
			"required":True,
			}),
		"email":forms.EmailInput(attrs = {
			"class":"form-control",
			"placeholder":"Enter emailid",
			"required":True,
			}),
		}
		
class ServiceForm(forms.ModelForm):
	class Meta:
		model= UserService
		fields=["car_name","service_type","price","quantity"]
		widgets = {
		"car_name":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"enter carname",
			}),
		"service_type":forms.TextInput(attrs= {
			"class":"form-control","placeholder":"enter service",
			}),

		"quantity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Quantity",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Price",
			}),
		}
class Userupdate(forms.ModelForm):
	class Meta:
		model=UserService
		fields=["car_name","service_type","price","quantity"]
		widgets = {
		"car_name":forms.Select(attrs= {
			"class":"form-control","placeholder":"select carname",
			}),
		"service_type":forms.Select(attrs= {
			"class":"form-control","placeholder":"select service",
			}),

		"quantity":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Quantity",
			}),
		"price":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Price",
			}),
		}