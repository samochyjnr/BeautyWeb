from django.urls import path
from beautyapp import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('about/', views.about, name = 'about'),
    path('product/', views.product, name = 'product'),
    
]
