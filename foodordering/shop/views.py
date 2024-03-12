from django.shortcuts import render
from shop.models import Category,Product
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def allcategories(request):
    c=Category.objects.all()
    return render(request,'category.html',{'category':c})
def allproducts(request,p):
    b=Category.objects.get(name=p)
    product=Product.objects.filter(category=b)
    return render(request,'product.html',{'c':b,'p':product})

def viewproduct(request,p):
    c=Product.objects.get(name=p)
    return render(request,'viewproduct.html',{'product':c})

def register(request):
        if (request.method == "POST"):
            u = request.POST['u']
            p = request.POST['p']
            cp = request.POST['cp']
            e = request.POST['e']
            if (p == cp):
                u = User.objects.create_user(username=u, password=p, email=e)
                u.save()
                return user_login(request)
            else:
                return HttpResponse("password not matching")
        return render(request, 'register.html')

def user_login(request):
    if (request.method == "POST"):
        name = request.POST['u']
        pass1 = request.POST['p']  # here we mentioned as pass1 because pass is a keyword
        user = authenticate(username=name, password=pass1)
        if user:
            login(request,user)
            return allcategories(request)
        else:
            messages.error(request, 'invalid credentials')
    return render(request,'login.html')

@login_required
def user_logout(request):
    logout(request)
    return user_login(request)

