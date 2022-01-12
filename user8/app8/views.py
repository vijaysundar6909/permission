from django.contrib.auth.models import User, auth, Group
from django.core.exceptions import PermissionDenied
from django.core.mail import message
from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import  routers
# Create your views

routers
def browser(request):
    if request.method == 'POST':
        fname = request.POST['first_name']
        lname = request.POST['last_name']
        name = request.POST['username']
        mail = request.POST['email']
        password = request.POST['password']
        Type = request.POST['type']
        user = User.objects.create_user(first_name=fname, last_name=lname, username=name, email=mail, password=password)
        print("user created")
        user.save()

        if Type == 'employee':
            group = Group.objects.get(name='employee_group')
            group.user_set.add(user)
            print("employee added")
        elif Type == 'staff':
            group = Group.objects.get(name="staff_group")
            group.user_set.add(user)
            print("staff added")
        return redirect('/')

    else:
        return render(request, "empreg.html")


def browser1(request):
    return render(request, "home.html")


def browser2(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        print("showed login")
        if user.groups.filter(name='employee_group'):
            auth.login(request, user)
            return render(request, 'home.html')
        else:
            return render(request, "empreg.html")
    else:
        return render(request, "login.html")


def next(request):
    return render(request, 'nextpage.html')


def browser5(request):
    if request.method == 'POST':
        uname = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=uname, password=password)
        print("showed login")
        if user.groups.filter(name='staff_group'):
            auth.login(request, user)
            return redirect( '/home_staff')
        else:
            return render(request, "empreg.html")
    else:
        return render(request, "login.html")


def browser3(request):
    auth.logout(request)
    print("showed")
    return redirect("/")


def browser4(request):
    if request.user.is_authenticated and request.user.groups.filter(name = "staff_group"):
        return render(request, 'home_staff.html')
    else:
        raise PermissionDenied
