from django.shortcuts import render
from .models import Point
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from pools.serializers import UserSerializer
from pools.permissions import IsOwner
from django.contrib.auth.models import User


def index(request):
    return render(request, 'index.html', {})


def home(request):
    points = Point.objects.filter()
    return render(request, 'home.html', {'points': points})


def contact(request):
    return render(request, 'contact.html', {})


def about(request):
    return render(request, 'about.html', {})


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)

        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        return (permissions.IsAuthenticated(), IsOwner(),)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            User.objects.create_user(**serializer.validated_data)

            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': 'Bad request',
            'message': 'User could not be created without data'
        }, status=status.HTTP_400_BAD_REQUEST)

