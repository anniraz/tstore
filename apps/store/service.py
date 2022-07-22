from django_filters import rest_framework as filters
from rest_framework.response import Response
from .models import Technology

from rest_framework.pagination import PageNumberPagination

class CharFilterInFilter(filters.BaseInFilter,filters.CharFilter):
    pass

class ProductFilter(filters.FilterSet):
    name=CharFilterInFilter(field_name='name',lookup_expr='in')
    category=CharFilterInFilter(field_name='category__title',lookup_expr='in')

    class Meta:
        model=Technology
        fields=['name','category']


class Paginations(PageNumberPagination):
    page_size=2
    max_page_size=1000

    def get_paginated_response(self, data):
        return Response({
            'links':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link()
            },
            'count':self.page.paginator.count,
            'results':data
        })
