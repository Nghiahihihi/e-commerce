from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment
from .serializers import PaymentSerializer
from order_service.models import Order

import uuid  # để tạo transaction_id giả lập

class ProcessPaymentView(APIView):
    def post(self, request):
        serializer = PaymentSerializer(data=request.data)
        if serializer.is_valid():
            order = serializer.validated_data['order']

            # Kiểm tra xem đơn đã thanh toán chưa
            if Payment.objects.filter(order=order).exists():
                return Response({"error": "Order already paid."}, status=status.HTTP_400_BAD_REQUEST)

            # Giả lập thanh toán thành công
            payment = Payment.objects.create(
                order=order,
                method=serializer.validated_data['method'],
                status='success',
                transaction_id=str(uuid.uuid4())
            )

            # Cập nhật trạng thái đơn hàng
            order.status = 'confirmed'
            order.save()

            return Response({
                "message": "Payment successful.",
                "payment_id": payment.id,
                "transaction_id": payment.transaction_id
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
