from django.urls import path, re_path
from .views import *
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register(r"users", UserViewSet, basename="user")
router.register(r"cats", CategoryViewSet, basename="cat")
# user_list = UserViewSet.as_view({"get": "list", "post": "create"})
# user_detail = UserViewSet.as_view({"get": "retrieve", "put": "update", "delete": "destroy"})

urlpatterns = [
    # path('cats/', CategorytCreateListView.as_view(), name="cats"),
    # path('cat/<int:pk>/', CategoryRetrieveUpdateDestroyApiView.as_view(), name="cat_detail"),
    path('foods/', FoodCreateListView.as_view(), name="foods"),
    path('food/<int:pk>/', FoodRetrieveUpdateDestroyApiView.as_view(), name="food_detail"),
    path('orders/', OrderCreateListView.as_view(), name="orders"),
    path('order/<int:pk>/', OrderRetrieveUpdateDestroyApiView.as_view(), name="order_detail"),
    path('order_items/', OrderItemCreateListView.as_view(), name="order_item"),
    path('order_item/<int:pk>/', OrderItemRetrieveUpdateDestroyApiView.as_view(), name="order_item_detail"),
    path('clients', ClientCreateListView.as_view(), name="clients"),
    path('client/<int:pk>/', ClientRetrieveUpdateDestroyApiView.as_view(), name="client_detail"),
    # path('users/', user_list, name="users_list"),
    # path('user/<int:pk>/', user_detail, name="user_detail"),
] + router.urls