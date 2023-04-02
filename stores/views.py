from django.shortcuts import render
from rest_framework import generics
from .models import Pizzeria
from .serializers import PizzeriaListSerializer, PizzeriaDetailSerializer, UserSerializer
from rest_framework.parsers import MultiPartParser
from django.contrib.auth import get_user_model
from rest_framework import permissions

# Create your views here.
class PizzeriaListAPIView(generics.ListAPIView):
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaListSerializer

class PizzeriaRetrieveAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer

class PizzeriaCreateAPIView(generics.CreateAPIView):
    parser_classes = [MultiPartParser]
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer

class PizzeriaRetrieveUpdateAPIView(generics.RetrieveUpdateAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()
    serializer_class = PizzeriaDetailSerializer

class PizzeriaDestroyAPIView(generics.DestroyAPIView):
    lookup_field = 'id'
    queryset = Pizzeria.objects.all()

class UserCreateView(generics.CreateAPIView):
    model = get_user_model()
    parser_classes = [MultiPartParser]
    permission_classes = [permissions.AllowAny]
    serializer_class = UserSerializer

class ExceptionLoggingMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Code to be executed for each request before
        # the view (and later middleware) are called.
        print(request.body)
        print(request.scheme)
        print(request.method)
        print(request.META)

        response = self.get_response(request)

        return response
   


    