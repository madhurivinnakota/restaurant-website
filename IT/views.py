from django.shortcuts import render,redirect
from .models import Orders
from django.contrib import messages
from django.http import HttpResponse



def index(request):
      
      return render(request, 'food\index.html')

def whychooseus(request):
      return render(request, 'food/whychooseus.html')

def exploremenu(request):
      return render(request, 'food/exploremenu.html')

def deliveryandpayment(request):
      return render(request, 'food/deliveryandpayment.html')

def followus(request):
      if request.method=="POST":
            names=request.POST.get('myName')
            email=request.POST.get('myEmail')
            phone_number=request.POST.get('myPhone')
            descrion=request.POST.get('mesg')
            query=Orders(name=names,email=email,phone_number=phone_number,descrion=descrion)
            query.save()
            messages.info(request,"thanks for contacting us")
            
            

      return render(request, 'food/followus.html')

