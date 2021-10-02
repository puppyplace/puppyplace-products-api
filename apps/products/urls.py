from django.urls import path
from django.urls.conf import include

from apps.products.views import ProductDetailView, ProductsView

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products-list'),
    path('products/<uuid:pk>', ProductDetailView.as_view(), name='products-detail'),
]
