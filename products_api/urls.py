from django.urls import path
from django.urls.conf import include

from apps.categories import urls as categories_urls
from apps.products import urls as products_urls


urlpatterns = [
    path('api/v1/', include(categories_urls)),
    path('api/v1/', include(products_urls)),
]
