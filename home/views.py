from django.shortcuts import render
from random_words import RandomWords
# Create your views here.
def index(request):
    context={}
    context['profiles'] = range(1, 5)
    context['profiless'] = range(6, 11)
    context['name']="Russell"
    return render(request,'home/index.html',context)
