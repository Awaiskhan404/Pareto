from django.shortcuts import render

# Create your views here.
def login(request):
    username=request.POST.get("email", "")
    password=request.POST.get("password", "")
    print(password)
    print(username)
    return render(request,'login/login.html')
def signup(request):
    firstname=request.POST.get("firstname","")
    print(firstname)
    return render(request,'login/signup.html')