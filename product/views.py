from django.shortcuts import render
from rest_framework import viewsets

from product.models import Product
from product.permissions import IsAdmin
from product.serializers import CreateProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = CreateProductSerializer
    permission_classes = [IsAdmin]


# class UpdatePublicationView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = CreateProductSerializer
#     permission_classes = [IsAdmin]
#
#
# class DeletePublicationView(viewsets.ModelViewSet):
#     queryset = Product.objects.all()
#     serializer_class = CreatePublicationSerializer
#     permission_classes = [IsAdmin]




    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [IsAuthenticated()]
    #     elif self.action in ['update','partial_update','destroy']:
    #         return [IsAuthorOrIsAdmin()]
    #     return []
    #
    # def get_serializer_class(self):
    #     if self.action == 'list':
    #         return PublicationListSerializer
    #     elif self.action == 'retrieve':
    #         return CreatePublicationSerializer