from rest_framework.pagination import CursorPagination


class PostPagination(CursorPagination):
    page_size = 5
    ordering = '-created_date'
