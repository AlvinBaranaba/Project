from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Contact
from django.contrib import messages
from django.http import HttpResponse

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

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering! We will be in touch soon.')
            return redirect('my_home')
        else:
            # Force display of errors
            return HttpResponse(f"<h1>Form Errors:</h1><pre>{form.errors.as_json()}</pre>")
    else:
        form = RegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
