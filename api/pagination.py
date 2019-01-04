from rest_framework import pagination


class PaginacaoVagas(pagination.PageNumberPagination):
    page_size = 2
    page_query_param = 'page'
    page_size_query_param = 'per_page'
    max_page_size = 5
