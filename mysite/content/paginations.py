from rest_framework.pagination import PageNumberPagination,CursorPagination


class smallpagination(CursorPagination):
    page_size=3
    page_query_param='page_size'
    ordering='-created_date'