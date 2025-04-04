from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from .serializers import OrderSerializer
from cart_service.models import Cart, CartItem
from customer_service.models import Customer

class CreateOrderView(APIView):
    def post(self, request, customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            cart = Cart.objects.get(customer=customer)
            cart_items = CartItem.objects.filter(cart=cart)
            if not cart_items.exists():
                return Response({"error": "Cart is empty."}, status=status.HTTP_400_BAD_REQUEST)
        except Customer.DoesNotExist:
            return Response({"error": "Customer not found."}, status=status.HTTP_404_NOT_FOUND)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        total_amount = 0
        order = Order.objects.create(customer=customer, total_amount=0)

        for cart_item in cart_items:
            item = cart_item.item
            quantity = cart_item.quantity
            price = item.price
            OrderItem.objects.create(
                order=order,
                item=item,
                quantity=quantity,
                price=price
            )
            total_amount += price * quantity

        order.total_amount = total_amount
        order.save()

        # Xoá giỏ hàng sau khi đặt
        cart_items.delete()

        serializer = OrderSerializer(order)
        return Response({
            "message": "Order created successfully.",
            "order": serializer.data
        }, status=status.HTTP_201_CREATED)

class CustomerOrderHistoryView(APIView):
    def get(self, request, customer_id):
        orders = Order.objects.filter(customer__id=customer_id).order_by('-order_date')
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)