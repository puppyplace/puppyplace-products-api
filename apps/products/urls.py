from django.urls import path
from django.urls.conf import include

from apps.products import views

urlpatterns = [
    path('products/', views.ProductsView.as_view(), name='products-list'),
    path(
        'products/<uuid:pk>',
        ProductsDetailView.as_view(),
        name='products-detail',
    ),
]
