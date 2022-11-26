from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,)
from lms.models import Student
from lms.serialisers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]