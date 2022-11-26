from rest_framework import serializers

from lms.models import Student, Curator


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