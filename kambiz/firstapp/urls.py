from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('product3d/', views.product3d, name='product'),
]
 