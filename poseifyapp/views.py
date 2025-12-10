from django.shortcuts import render, redirect
from .models import Contact

# Create your views here.
def home(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        message=request.POST.get('message')

        query=Contact(name=name,email=email,subject=subject,message=message)
        query.save()
        return redirect("/")
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def team(request):
    return render(request,'team.html')