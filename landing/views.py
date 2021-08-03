from django.shortcuts import render
from account.models import Vidoes
# Create your views here.

def home(request):
    contex = { 'videos' : Vidoes.objects.all()}
    return render(request,'landing/index.html',contex)