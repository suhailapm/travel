from django.shortcuts import render
from .models import Place,People
# Create your views here.


from django.http import HttpResponse
def demo(request):
    #obj=Place.objects.all()
    var=People.objects.all()
    return render(request,"index.html",{'result':var})
#def about(request):
   # return render(request,"about.html")
#def sample(request):
  #  return HttpResponse("its another view")
#def addition(request):
#    x=int(request.GET['num1'])
 #   y=int(request.GET['num2'])
 #   res=x+y
 #   return render(request,"result.html",{'result':res})