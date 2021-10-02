from django.urls import path

from apps.categories.views import CategoryDetailView, CategoryView, ProductPerCategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories-list'),
    path('categories/<uuid:pk>', CategoryDetailView.as_view(), name='category-detail'),
    path(
        'categories/<uuid:category_id>/products',
        ProductPerCategoryView.as_view(),
        name='categorie-product-list',
    ),
]
