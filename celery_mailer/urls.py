from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.Students_list, name='student_list'),
    
]
