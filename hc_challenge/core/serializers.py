from rest_framework import serializers
from core.models import Report, ReportResponse
from django.contrib.auth.models import User

class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = ['id', 'message', 'author', 'supervisors']

class ReportResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportResponse
        fields = ['id', 'message', 'report', 'author']

class UserSerializer(serializers.ModelSerializer):
    reports = serializers.PrimaryKeyRelatedField(many=True, 
        queryset=Report.objects.all)
        
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name']