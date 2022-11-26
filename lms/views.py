from django.db.models import F
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,)
from lms.models import Student, Curator
from lms.permissions import IsAdminOrReadOnly, IsCuratorOrReadOnly
from lms.serialisers import StudentSerializer, CuratorSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsCuratorOrReadOnly]

class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [IsAdminOrReadOnly]
