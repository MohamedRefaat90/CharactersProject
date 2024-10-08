# pagination.py

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 5  # Set the default page size
    page_size_query_param = 'num_of_items'  # Allow clients to change page size via query parameter
    max_page_size = 100  # Set the maximum page size
