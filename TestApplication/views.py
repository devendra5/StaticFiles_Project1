from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import datetime
import os
#-------------------------> This Project Main is : Working with templates
# Create your views here.
"""
def wish(request):
    date = datetime.datetime.now()
    my_dict = {'insert_date':date}
    return render(request,'TestAPp/Wish.html',context = my_dict)

def wish(request):
    date = datetime.datetime.now()
    my_dict = {'insert_date':date}
    return render(request,'TestApp/Wish.html',context = my_dict}
"""
def wish(request):
    # to find the current the data and time is :
    date = datetime.datetime.now()
    msg = "Hello Guest!!! Very Very !!! ......!"
    # h = int(date.strftime('%H'))
    h = int(date.strftime('%H'))
    if h>12:
        msg += "Good Morning!"
    elif h>16:
        msg += "Good AfterNoon"
    elif h>20:
        msg += "Good Evening!"
    else:
        msg += "Good Night!"
    my_dict = {'insert_date':date,'insert_msg':msg}
    return render(request,'TestApp1/Wish.html',context=my_dict)



