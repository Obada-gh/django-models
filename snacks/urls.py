from django.urls import path
from .views import  snackView , snack_Detail_View


urlpatterns = [
   
    path('', snackView.as_view(), name='view'), 
    path('<int:pk>/', snack_Detail_View.as_view(), name='detailView'), 

]