from django.shortcuts import render
# Create your views here.
def index(request):
    context={}
    context['profiles'] = range(1, 5)
    context['profiless'] = range(6, 11)
    context['name']="Russell"
    return render(request,'home/index.html',context)
def services(request):
    context={}
    context['services']=range(1,5)
    return render(request, 'services/services.html',context)