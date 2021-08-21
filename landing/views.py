from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from account.models import Vidoes
from django.views.generic import ListView , DetailView
from django.core.paginator import Paginator
# Create your views here.

class ListVideo(ListView):
    model = Vidoes
    template_name = "landing/index.html"
    paginate_by = 2

# def home(request,page=None):
#     name = request.GET.get("name")
#     objects = Vidoes.objects.all()
#     objects = Paginator(objects,2)
#     page_number = page
#     page_obj = objects.get_page(page_number)
#     contex = { 'videos' : page_obj}
#     return render(request,'landing/index.html',contex)

class DetailVideo(DetailView):
    model = Vidoes
    template_name = "landing/single.html"

# def detail(request,pk_id):
#     video = get_object_or_404(Vidoes, pk=pk_id )
#     return render(request, "landing/single.html", {'video':video})

def multi(request,num):
    num = int(num)
    num += 1
    contex = []
    for i in range(1,num):
        tmp = []
        for j in range(1,num):
            tmp.append(j*i)
        contex.append(tmp)
    return render(request, "contex.html", {"contex" : contex})
# contex = [
# [1,2,3],
# [1,2,3],
# [1,2,3],
# ]