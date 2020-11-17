from rest_framework import serializers
from core.models import Report, ReportResponse
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']

class ReportResponseSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    class Meta:
        model = ReportResponse
        fields = ['id', 'message', 'report', 'author']

class ReportSerializer(serializers.ModelSerializer):
    author = UserSerializer()
    supervisors = UserSerializer(many=True)
    responses = ReportResponseSerializer(many=True)
    class Meta:
        model = Report
        fields = ['id', 'message', 'author', 'supervisors', 'responses']

