import math

from rest_framework import pagination


class StandardResultsPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 1000
    page_size_query_param = "page_size"

    def get_paginated_response(self, data):
        response=super(StandardResultsPagination, self).get_paginated_response(data)
        print(type(response.data))
        response.data["count"]=self.page.paginator.count
        response.data["no_of_pages"]=math.ceil(response.data["count"]/self.page_size)
        return response