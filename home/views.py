from django.shortcuts import render
# Create your views here.
def index(request):
    context={}
    context['profiles'] = range(1, 5)
    context['profiless'] = range(6, 11)
    context['name']="Russell"
    return render(request,'home/index.html',context)
def services(request):
    
    services=range(1,5)
    name=["Daniel J","Harry M","Jesse B","Hooper E","Jean-Pierre B"]
    return render(request, 'services/services.html',{
        'name':name,
        'services':services,
    })