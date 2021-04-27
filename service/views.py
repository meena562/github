from django.shortcuts import render,redirect
from service.forms import UsForm,ServiceForm,Userupdate
from django.core.mail import send_mail
from carservice import settings
from django.contrib import messages
from django.contrib.auth.models import User
from service.models import UserService
from django.contrib.auth.decorators import login_required

# Create your views here
def home(request):
	return render(request,'services/home.html')

def about(request):
	return render(request,'services/about.html')

def contact(request):
	return render(request,'services/contact.html')

def registration(request):
	if request.method=="POST":
		p=UsForm(request.POST)
		if p.is_valid():
			p.save()
			return redirect('/log')
			
	p=UsForm()
	return render(request,'services/register.html',{'u':p})

def Service(request):
	if request.method=="POST":
		j=ServiceForm(request.POST,request.FILES)
		if j.is_valid():
			i=j.save(commit=False)
			i.uid_id=request.user.id
			i.save()
			return redirect('/showdata')
	j=ServiceForm()
	return render(request,'services/Services.html',{'u':j})

def deletedata(req,st):
	data=UserService.objects.get(id=st)
	data.delete()
	return redirect('/cr')



def showinfo(req):
	data=UserService.objects.all()
	return render(req,'services/showdata.html',{'info':data})

def infodelete(req,et):
	data=UserService.objects.get(id=et)
	if req.method == "POST":
		data.delete()
		return redirect('/showdata')
	return render(req,'services/userdelete.html',{'sd':data})

def userupdate(up,si):
	t=UserService.objects.get(id=si)
	if up.method=="POST":
		d=Userupdate(up.POST,instance=t)
		if d.is_valid():
			d.save()
			return redirect('/showdata')
	d=Userupdate(instance=t)
	return render(up,'services/updateuser.html',{'us':d})



def profile(req):
	return render(req,'services/profile.html')
1															
