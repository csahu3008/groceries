from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import GroceryViewSet,SearchGroceryItemsView

router = DefaultRouter()
urlpatterns=[
    path('search-items',SearchGroceryItemsView.as_view(),name='search')
]
router.register(r'grocery_item', GroceryViewSet, basename='Grocery_items')
urlpatterns += router.urls