from django.shortcuts import render,redirect
from .models import Vehicle
from .forms import VehicleForm
# Create your views here.

def home(request):
    return render(request,'bikes/home.html')

def sell(request):
    form = VehicleForm()
    if request.method == 'POST':
        vehicle_form = VehicleForm(request.POST)
        if vehicle_form.is_valid():
            vehicle_form.save()
            return redirect('home')
    
    return render(request,'bikes/sell.html',{'form':form})

def buy(request):
    return render(request,'bikes/buy.html')