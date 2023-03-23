import django_filters
from django.shortcuts import render
from rest_framework.generics import *
from main.serializers import *
from main.models import *
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly, IsAdminUser
from django.contrib.auth.models import User
from rest_framework.authentication import *
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .permissions import *
from rest_framework import filters

# class CategorytCreateListView(ListCreateAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

# class CategoryRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     lookup_field = "pk"

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FoodCreateListView(ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class FoodRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    lookup_field = "pk"



class ClientCreateListView(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fileds = "__all__"
    ordering = ["full_name"]
    # def get_queryset(self):
    #     queryset = Client.objects.all()
    #     name = self.request.query_params.get("name")
    #     if name is not None:
    #            return Client.objects.filter(full_name__icontains=name) 
    #     return queryset

class ClientRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = "pk"



class OrderCreateListView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['is_paid', 'shipping', 'client']

    # def get_queryset(self):
    #     return Order.objects.filter(is_paid=True)
    #     return super().get_queryset()



class OrderRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = "pk"



class OrderItemCreateListView(ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemRetrieveUpdateDestroyApiView(RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    lookup_field = "pk"


class RegisterAPIView(APIView):
    permission_classes = (AllowAny, )

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({})

class LoginAPIView(APIView):
    permission_classes = (AllowAny, )
        

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = serializer.save()
        return Response({"key": token.key})

class LogoutAPIView(APIView):
    def post(self, request):
        request.user.auth_token.delete()        
        return Response({"detail": "Successfully loged out"})

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAdminUser, )

    def create(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({}, status=status.HTTP_201_CREATED)

    # def get_permissions(self):
    #     if self.action == "list":
    #         permission_classes = [AllowAny]
    #     else:
    #         permission_classes = [IsAdminUser]
    #     return [permission() for permission in permission_classes]

    @action(detail=True, methods=['post'], permission_classes=[IsAdminOrSelf])
    def set_password(self, request, pk):
        user = self.get_object()
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user.set_password(serializer.validated_data["password"])
            user.save()
            return Response({"status": "Password Set"})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['get'])
    def recent_users(self, request):
        return Response({"detail" "Working..."})





    # def list(self, request):
    #     users = User.objects.all()
    #     serializer = UserSerializer(users, many=True)
    #     return Response(serializer.data)
    
    # def create(self, request):
    #     serializer = RegisterSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response({}, status=status.HTTP_201_CREATED)

    # def retrieve(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     serializer = UserSerializer(instance=user)
    #     return Response(serializer.data)

    # def update(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     serializer = UserSerializer(instance=user, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)

    # def destroy(self, request, pk):
    #     user = get_object_or_404(User, pk=pk)
    #     user.delete()
    #     return Response({}, status=status.HTTP_204_NO_CONTENT)