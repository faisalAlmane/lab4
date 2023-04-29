from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path('taxrate', views.taxrate,name="taxrate"),
    path('<int:num>', views.taxn),   
   

]