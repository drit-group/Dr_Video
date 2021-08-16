from django.shortcuts import render
from account.models import Vidoes

from django.core.paginator import Paginator
# Create your views here.

def home(request,page=None):
    name = request.GET.get("name")
    objects = Vidoes.objects.all()
    objects = Paginator(objects,2)
    page_number = page
    page_obj = objects.get_page(page_number)
    contex = { 'videos' : page_obj}
    return render(request,'landing/index.html',contex)

def multi(request):
    num = request.GET.get("num")
    num += 1
    contex = []
    for i in range(1,num):
        tmp = []
        for j in range(1,num):
            tmp.append(j*i)
        contex.append(tmp)
    
# contex = [
# [1,2,3],
# [1,2,3],
# [1,2,3],
# ]