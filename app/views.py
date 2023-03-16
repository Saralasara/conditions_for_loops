from django.shortcuts import render

# Create your views here.

def conditions(request):
    d={'a':1909,'b':2090,'c':20099}
    return render(request,'conditions.html',d)


def loops(request):
    d={'name':'ASHU'}
    return render(request,'loops.html',d)