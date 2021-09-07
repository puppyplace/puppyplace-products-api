from django.urls import path
from django.urls.conf import include

from apps.categories import urls as categories_urls

urlpatterns = [
    path('api/v1/', include(categories_urls)),
]
