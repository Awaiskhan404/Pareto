from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.models import User, auth
# Create your views here.
def login(request):
    # username=request.POST.get("email", "")
    # password=request.POST.get("password", "")
    # user=auth.authenticate(username=username,password=password)
    # if user is not None:
    #     auth.login(request,user)
    #     return redirect('/dashboard')
    # else:
    #     messages.info(request,'Invalid Credentials')
    #     return redirect('/')

    return render(request,'login/login.html')

def handle_login(request):
    if request.method=='POST':

        username=request.POST.get("email", "")
        password=request.POST.get("password", "")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/dashboard')
        else:
            messages.error(request,"Invalid Credentials. Try again")
            return redirect('/login',messages)
    else:
        return HttpResponse("Forbidden. You are not allowed to send this request. Try through login page")
    return render(request,'login/login.html')
def signup(request):
    
    return render(request,'login/signup.html')
def handle_signup(request):
    if request.method=='POST':
        firstname=request.POST.get("firstname","")
        lastname=request.POST.get("lastname","")
        email=request.POST.get("email","")
        password1=request.POST.get("password1","")
        password2=request.POST.get("password2","")
        if password1==password2:
            if User.objects.filter(username=email).exists():
                messages.error(request,"email already exists. Try login")
                return redirect('/signup',messages)
            elif User.objects.filter(email=email).exists():
                messages.error(request,"email already exists. Try login")
                return redirect('/signup',messages)
            else:
                user=User.objects.create_user(username=email,password=password1,email=email,first_name=firstname,last_name=lastname)   
                user.save()
                messages.success(request,"Your account has been created. Login here")
                return redirect('/login',messages)
        else:
            messages.error(request,"Password did not math")
            return redirect('/signup',messages)        
    else:
        return HttpResponse("Forbidden. You are not allowed to send this request")