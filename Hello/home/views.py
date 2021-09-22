from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages

# Create your views here.   
def index(request):
    context = {
        'variable1':'sent Ho gya',
        'variable2':'sent Ho gya 2'
    }      
    return render(request, 'index.html', context)
    # return HttpResponse("this is homepage")

def about(request):
     return render(request, 'about.html',)

def services(request):
     return render(request, 'services.html',)

def contact(request):
     if request.method == 'POST':
          name = request.POST.get('name')
          email = request.POST.get('email')
          phone = request.POST.get('phone')
          contact = Contact(name=name, email=email, phone=phone, date=datetime.today())
          contact.save()
          messages.success(request, 'Your Meassage has been Sent Successfully !!')
     return render(request, 'contact.html',)