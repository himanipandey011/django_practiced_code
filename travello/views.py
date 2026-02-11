from django.shortcuts import render
from .models import Destiination



# Create your views here.
# def home(request):
#    return render(request,'index.html',{'price':700} )


# Create your views here.
def home(request):

   dest1= Destiination()
   dest1.name = 'Plans'
   
   return render(request,'index.html',{'dest1':dest1} )