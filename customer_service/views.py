from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import CustomerSerializer
from .models import Customer

class RegisterCustomer(APIView):
    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "message": "Customer registered successfully!",
                "data": serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginCustomer(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email or not password:
            return Response({'error': 'Email and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            customer = Customer.objects.get(email=email)
        except Customer.DoesNotExist:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        # So sánh mật khẩu (tạm thời chưa hash)
        if customer.password != password:
            return Response({'error': 'Invalid email or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response({
            'message': 'Login successful!',
            'customer_id': customer.id,
            'name': customer.name,
            'email': customer.email
        }, status=status.HTTP_200_OK)



def home(request):
    return render(request, 'home.html')

def register_form(request):
    return render(request, 'register.html')

def login_form(request):
    return render(request, 'login.html')

def product_list(request):
    return render(request, 'products.html')

def view_cart(request):
    return render(request, 'cart.html')

def checkout_form(request):
    return render(request, 'checkout.html')

class CustomerListView(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)