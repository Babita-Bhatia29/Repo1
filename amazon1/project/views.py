from django.shortcuts import render
from project.models import Category,Product,Query,Offer,carousel
# Create your views here.
def indexpage(request):
    a=Category.objects.all()
    b=Product.objects.all()
    c=carousel.objects.all()
    d=Offer.objects.all()
    e=Query.objects.all()
    return render(request,"index.html",{'a':a, "b":b, "c":c, "d":d,"e":e})
def viewproduct(request,myid):
    x=Product.objects.filter(id=myid)
    return render(request,"viewproduct.html",{'x':x[0]})