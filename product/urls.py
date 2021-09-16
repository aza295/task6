from django.urls import path

from product.views import ProductViewSet

urlpatterns = [
    path('publications/', ProductViewSet.as_view(
    {'get': 'list',
     'post': 'create'}
    )),
    path('publications/<int:pk>/', ProductViewSet.as_view(
        {'get': 'retrieve',
         'put': 'update',
         'patch': 'partial_update',
         'delete': 'destroy'}
    )),
]