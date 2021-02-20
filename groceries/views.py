from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import GroceryItemSerializer
from rest_framework import filters
from .models import GroceryItem
from django.db.models import Q
from rest_framework import pagination
from rest_framework.generics import ListAPIView
class GroceryViewSet(viewsets.ModelViewSet):
    queryset = GroceryItem.objects.all()
    serializer_class = GroceryItemSerializer




class CustomPagination(pagination.PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_query_param = 'p'

class SearchGroceryItemsView(ListAPIView):
    serializer_class = GroceryItemSerializer
    filter_backends = [filters.OrderingFilter]
    pagination_class=CustomPagination
    ordering_fields = ['price', 'createdAt']
    def get_queryset(self):
        queryset = GroceryItem.objects.all()
        search_query = self.request.query_params.get('search_query', None)
        if search_query is not None:
            queryset = queryset.filter(Q(title__iexact=search_query)|Q(description__iexact=search_query))
        return queryset