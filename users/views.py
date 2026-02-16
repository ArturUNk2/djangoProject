from django.shortcuts import render

# Create your views here.

def  registerview(reguest):
    return render(reguest, 'register.html')