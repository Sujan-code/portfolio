from django.shortcuts import render,redirect
from .models import *
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def Home(request):
    return render(request, 'mainapp/main.html')

def Service(request,pk):
    servicee = service.objects.get(id=pk)
    context = {'servicee':servicee}
    return render(request, 'mainapp/servicedetail.html', context)

def Services(request):
    services = service.objects.all()
    context = {'services':services}
    return render(request, 'mainapp/services.html', context)

def Work(request,pk):
    workk = work.objects.get(id=pk)
    context = {'workk':workk}
    return render(request, 'mainapp/workdetail.html', context)

def Works(request):
    works = work.objects.all()
    context = {'works':works}
    return render(request, 'mainapp/work.html', context)


def Blog(request,pk):
    blogg = blog.objects.get(id=pk)
    context = {'blogg':blogg}
    return render(request, 'mainapp/blogdetail.html', context)

def Blogs(request):
    blogs = blog.objects.all()
    context = {'blogs':blogs}
    return render(request, 'mainapp/blog.html', context)

def About(request):
    educations = education.objects.all()
    experiences = experience.objects.all()
    context = {'educations':educations,'experiences':experiences}

    return render(request, 'mainapp/about.html', context)

def Contact(request):

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Message Sent ' ) 

            return redirect('home')

    context = {'form': form}
    return render(request, 'mainapp/contact.html', context)


