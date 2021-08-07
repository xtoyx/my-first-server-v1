from django.urls import path
from . import  views

urlpatterns = [
    path('',views.HomePageView , name="home"),
    path('projects/',views.ProjectsPageView, name="projects"),
    path('home/',views.HomePageView, name="home"),
    path('protfilo/',views.ProtFiloPageView , name="protfilo"),
    path('precent/',views.PrecentPageView , name="precent"),
    path('test/',views.TestPageView , name="test"),
]