from django.shortcuts import render
from django.views.generic import  ListView , DetailView
from .models import Snack


class snackView (ListView): 
    template_name="snack_list.html"  
    model = Snack


class snack_Detail_View (DetailView): 
    template_name="snack_detail.html"  
    model = Snack
