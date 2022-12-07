import math
from rest_framework.pagination import PageNumberPagination

class PageNumberPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    

class CustomResultsSetPagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = 'page_size'
    page_query_param = 'p'


def get_pagination_result(paginator, total_items):
    items_per_page = paginator.page_size
    try:
        current_page = paginator.page.number
    except  AttributeError:
        current_page = 1
    total_page = math.ceil(total_items/items_per_page)

    return {
        'current_page': current_page,      
        'total_page': total_page
    }

