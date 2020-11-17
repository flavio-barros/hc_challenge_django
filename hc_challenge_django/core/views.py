from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics, viewsets
from core.models import Report, ReportResponse
from core.serializers import ReportSerializer, ReportResponseSerializer, UserSerializer
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from core.pagination import CustomOffsetPagination
from django.db.models import Q

class ReportViewSet(viewsets.ReadOnlyModelViewSet):
    #queryset = Report.objects.all()
    serializer_class = ReportSerializer
    pagination_class = CustomOffsetPagination

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)
        pagination_offset = self.request.query_params.get('pagination_offset', None)
        pagination_limit = self.request.query_params.get('pagination_limit', None)

        if(user_id):
            queryset = Report.objects.filter(
                Q(author=user_id) | Q(supervisors=user_id) | Q(responses__author=user_id))
            return queryset
        else:
            queryset = Report.objects.all()
            return queryset

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
