from django.urls import path
from django.urls.conf import include

from apps.categories.views import CategoryDetailView, CategoryView

urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories-list'),
    path(
        'categories/<uuid:pk>',
        CategoryDetailView.as_view(),
        name='category-detail',
    ),
]
