from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from account.models import Article
from django.views.generic import ListView , DetailView
#from django.core.paginator import Paginator
# Create your views here.

class ListVideo(ListView):
    model = Article
    template_name = "landing/main.html"
    paginate_by = 2
<<<<<<< Updated upstream
    #use oBject_list as a oBjectlist
=======

def home(request,page=None):
    name = request.GET.get("name")
    objects = Article.objects.all()
    objects = Paginator(objects,2)
    page_number = page
    page_obj = objects.get_page(page_number)
    contex = { 'Article' : page_obj}
    return render(request,'landing/main.html',contex)
>>>>>>> Stashed changes

class DetailVideo(DetailView):
    model = Article
    template_name = "landing/single.html"
    #use Article as a oBjectlist.Becouse of it's one ithem

# def home(request,page=None):
#     name = request.GET.get("name")
#     objects = Vidoes.objects.all()
#     objects = Paginator(objects,2)
#     page_number = page
#     page_obj = objects.get_page(page_number)
#     contex = { 'Article' : page_obj}
#     return render(request,'landing/index.html',contex)



# def detail(request,pk_id):
#     video = get_object_or_404(Vidoes, pk=pk_id )
#     return render(request, "landing/single.html", {'video':video})

<<<<<<< Updated upstream
=======

# contex = [
# [1,2,3],
# [1,2,3],
# [1,2,3],
# ]
>>>>>>> Stashed changes
