from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse
from account.models import Film
from django.views.generic import ListView , DetailView
# from mixins import 
#from django.core.paginator import Paginator
# Create your views here.

class ListVideo(ListView):
    # model = Film
    template_name = "landing/index.html"
    paginate_by = 2
    def get_queryset(self):
        return Film.objects.filter(status='p')




class DetailVideo(DetailView):
    # model = Film
    template_name = "landing/single.html"
    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Film,slug=slug,status='p')
    #use Film or object as an objectlist.Becouse of it's one ithem

# def home(request,page=None):
#     name = request.GET.get("name")
#     objects = Vidoes.objects.all()
#     objects = Paginator(objects,2)
#     page_number = page
#     page_obj = objects.get_page(page_number)
#     contex = { 'Film' : page_obj}
#     return render(request,'landing/index.html',contex)



# def detail(request,pk_id):
#     video = get_object_or_404(Vidoes, pk=pk_id )
#     return render(request, "landing/single.html", {'video':video})
