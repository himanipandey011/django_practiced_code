from django.shortcuts import render
from django.http import HttpResponse

# def home(request):
#     return HttpResponse("Hello")

def home(request):
   return render(request,'index1.html',{'name':'Himani'})

# def add(request):
#     val1 = request.GET['num1']
#     val2 = request.GET['num2']
#     res = int (val1) +int (val2)
#     return  render(request,"result.html",{'result':res})

def add(request):
    val1 = request.POST['num1']
    val2 = request.POST['num2']
    res = int (val1) +int (val2)
    return  render(request,"result.html",{'result':res})

