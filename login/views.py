from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def login(request):
    username=request.POST.get("email", "")
    password=request.POST.get("password", "")
    user=auth.authenticate(username=username,password=password)
    if user is not None:
        auth.login(request,user)
        return redirect('/dashboard')
    print(password)
    print(username)

    return render(request,'login/login.html')
def signup(request):
    firstname=request.POST.get("firstname","")
    print(firstname)
    return render(request,'login/signup.html')