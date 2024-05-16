from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('products-list', views.productsLists, name= 'productds_List'),
    path('brand/<str:Brand_name>', views.brand_mob, name = 'brandMob'),
    path('base', views.base),
    path('product-details/<int:pk>,<str:Brand_name>', views.productDetails, name = 'products_details'),
    
    
      
]