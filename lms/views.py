from django.db.models import F
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,)
from rest_framework.response import Response

from lms.models import Student, Curator, Group
from lms.permissions import IsAdminOrReadOnly, IsCuratorOrReadOnly
from lms.serialisers import StudentSerializer, CuratorSerializer, GroupSerializer


class StudentViewSet(viewsets.ModelViewSet):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsCuratorOrReadOnly]

class CuratorViewSet(viewsets.ModelViewSet):
    queryset = Curator.objects.all()
    serializer_class = CuratorSerializer
    permission_classes = [IsAdminOrReadOnly]

    @action(detail=True)
    def get_first_name(self, request,pk=None):
        curator = self.get_object()
        return Response(curator.first_name)

    @action(detail=True)
    def give_like(self, request, pk=None):
        curator = self.get_object()
        if curator.liked_me.filter(id=request.user.id).exists():
            return Response(False)
        else:
            curator.liked_me.add(request.user)
            return Response(True)


    @action(detail=True)
    def count_like(self, request, pk=None):
        curator = self.get_object()

        return Response(curator.liked_me.count())


    @action(detail=True)
    def take_like(self, request, pk=None):
        curator = self.get_object()
        if curator.liked_me.filter(id=request.user.id).exists():
            curator.liked_me.remove(request.user)
            return Response(True)
        else:

            return Response(False)

# curator.liked_me.filter(id=request.user.id).exists()
# curator.liked_me.count()
class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAdminOrReadOnly]
    lookup_field = 'id'

    @action(detail=True)
    def students(self, request,id=None):
        group = self.get_object()
        students = group.student.all()
        serializer = StudentSerializer(data=students, many=True)
        serializer.is_valid()
        return Response(serializer.data)

    @action(detail=True)
    def curator(self, request,id=None):
        group = self.get_object()
        curator = group.direction.curator

        return Response(curator.id)

    # t.me/dugeru42