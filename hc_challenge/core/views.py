from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from core.models import Report, ReportResponse
from core.serializers import ReportSerializer, ReportResponseSerializer

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer