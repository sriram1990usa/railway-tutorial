from django import urls
from django.contrib import admin
from django.urls import path, re_path
from .views import *
app_name = 'home'
urlpatterns = [
    path('', hom, name="hom"),    
    path('addR/', addR, name="addR"),
    path('addST/', addST),
    path('addT/', addT, name="addT"),
    path('addRT/', addRT),  
    re_path(r'^search$', search, name="search"),    
    re_path(r'^pnr$', pnr, name="pnr"),
    re_path(r'^search/trains$', getTrains),    
    path('search/trains/cva/', cva),    
    re_path(r'^search/book1$', book1, name="book1"),  
    re_path(r'^search/book1/book$', book),       
    re_path(r'^schedule$', schedule),        
    path('schedule/trains/', getTinfo),
    re_path(r'^cancel$', cancel, name="cancel"),

    path('cancel/cancel/cn/', cn),
]
