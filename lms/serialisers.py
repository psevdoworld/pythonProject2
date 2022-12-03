from rest_framework import serializers

from lms.models import Student, Curator, Group


class StudentSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Student
        fields = '__all__'

class CuratorSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Curator
        fields = '__all__'


class GroupSerializer(
    serializers.ModelSerializer
):
    class Meta:
        model = Group
        fields = '__all__'