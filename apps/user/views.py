from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserAPIView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()