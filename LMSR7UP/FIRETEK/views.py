from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request,'index.html')
    # mapeamento de webreturn render(request,'./pages/index.html')


