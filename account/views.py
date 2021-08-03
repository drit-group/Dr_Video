from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def wellcome(request):
    data = {
        'name' : 'nima',
        'grade' : '12'
    }
    return render(request,"index.html",data)