from rest_framework.pagination import CursorPagination


class PostPagination(CursorPagination):
    page_size = 2
    ordering = '-created_date'
