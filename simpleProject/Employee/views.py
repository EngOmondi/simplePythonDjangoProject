from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Employee_Info(request):
    return HttpResponse("<h1>Welcome to TechVidvan Employee Portal</h1>")
def Employee_Details(request):
    context = {
    "first_name" : "Fidel",
              }
    return render (request,'Employee_details.html',context)
