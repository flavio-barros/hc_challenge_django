from rest_framework.pagination import LimitOffsetPagination

class CustomOffsetPagination(LimitOffsetPagination):
    limit_query_param = 'pagination_limit'
    offset_query_param = 'pagination_offset'