from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartItem
from .serializers import CartSerializer, CartItemSerializer
from customer_service.models import Customer
from item_service.models import Item

# Xem giỏ hàng theo customer_id
class ViewCart(APIView):
    def get(self, request, customer_id):
        try:
            cart = Cart.objects.get(customer__id=customer_id)
        except Cart.DoesNotExist:
            return Response({"error": "Cart not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart)
        return Response(serializer.data)


# Thêm sản phẩm vào giỏ
class AddToCart(APIView):
    def post(self, request, customer_id):
        item_id = request.data.get('item_id')
        quantity = int(request.data.get('quantity', 1))

        try:
            customer = Customer.objects.get(id=customer_id)
            item = Item.objects.get(id=item_id)
        except (Customer.DoesNotExist, Item.DoesNotExist):
            return Response({"error": "Invalid customer or item ID."}, status=status.HTTP_400_BAD_REQUEST)

        cart, created = Cart.objects.get_or_create(customer=customer)

        cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

        return Response({"message": "Item added to cart successfully."}, status=status.HTTP_200_OK)


# Xoá sản phẩm khỏi giỏ
class RemoveFromCart(APIView):
    def delete(self, request, customer_id, item_id):
        try:
            cart = Cart.objects.get(customer__id=customer_id)
            cart_item = CartItem.objects.get(cart=cart, item__id=item_id)
        except (Cart.DoesNotExist, CartItem.DoesNotExist):
            return Response({"error": "Item not found in cart."}, status=status.HTTP_404_NOT_FOUND)

        cart_item.delete()
        return Response({"message": "Item removed from cart."}, status=status.HTTP_200_OK)
