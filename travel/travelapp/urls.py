from . import views
from django.urls import path

urlpatterns = [
    path('',views.demo,name='demo'),
   #path('about/',views.about,name='about'),
  #  path('sample',views.sample,name='sample')
    #path('add/',views.addition,name='addition')
]