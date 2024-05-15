from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('products-list', views.productsLists, name= 'productds_List'),
    path('brand/<str:Brand_name>', views.BrandMob, name = 'brandMob'),
    path('base', views.base)
    
      
]