from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

class OptionalPagination(PageNumberPagination):
    page_size = 5  # Número de elementos por página

    def paginate_queryset(self, queryset, request, view=None):
        # Obtener los parámetros de ordenamiento
        order = request.query_params.get('order', None)
        orderby = request.query_params.get('orderby', 'asc')

        if order:
            if orderby == 'desc':
                order = f'-{order}'
            queryset = queryset.order_by(order)
        
        if 'page' not in request.query_params:
            return None
        return super().paginate_queryset(queryset, request, view)

    def get_paginated_response(self, data):
        return super().get_paginated_response(data)