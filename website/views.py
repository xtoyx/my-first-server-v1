from django.shortcuts import render
from .models import ProjectsIdea , PrecentCHECKD


def HomePageView(request):
    return render(request,'home.html',{})
    

def ProjectsPageView(request): # new
    all_ideas = ProjectsIdea.objects.all
    return render(request,'projects.html',{'all':all_ideas})


def PrecentPageView(request): # new
    all_precents = PrecentCHECKD.objects.all
    return render(request ,'precent.html', {'precnet_all':all_precents})

def ProtFiloPageView(request): # new
    return render(request ,'prot-file.html', {})
    
def TestPageView(request):
    return render(request,'test2.html',{})