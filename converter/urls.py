from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_signs/', views.get_signs, name='get_signs'),
]
