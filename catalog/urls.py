from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, index, products, product_info

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
    path('product/<int:pk>/', product_info, name='product_info'),
    path('home/', home, name='home'),
    path('contacts/', contacts, name='contacts'),
]
