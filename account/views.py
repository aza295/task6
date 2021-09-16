from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response

from account.serializers import RegistrationSerializer, ActivationSerializer, LoginSerializer


class RegistrationView(APIView):
    def post(self, request):
        serializer = RegistrationSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Activation code was Send', status=201)
        return Response(serializer.errors, status=400)

class ActivationView(APIView):
    def post(self, request):
        serializer = ActivationSerializer(data= request.data)
        if serializer.is_valid():
            serializer.activate()
            return Response('User Successfuly Activated')
        return Response(serializer.errors, status=400)

class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer