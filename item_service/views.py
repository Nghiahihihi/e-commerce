from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ItemSerializer
from .models import Item

class AddItemView(APIView):
    def post(self, request):
        data = request.data

        if isinstance(data, list):  # ✅ Nếu gửi danh sách
            created_items = []
            for item_data in data:
                serializer = ItemSerializer(data=item_data)
                if serializer.is_valid():
                    item = serializer.save()
                    created_items.append(serializer.data)
                else:
                    return Response(serializer.errors, status=400)
            return Response({
                "message": f"{len(created_items)} items added successfully!",
                "items": created_items
            }, status=201)

        # ✅ Nếu chỉ là 1 sản phẩm
        serializer = ItemSerializer(data=data)
        if serializer.is_valid():
            item = serializer.save()
            return Response({
                "message": "Item added successfully!",
                "item_id": item.id,
                "data": serializer.data
            }, status=201)
        return Response(serializer.errors, status=400)

class ItemListView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)
    
class ItemDetailView(APIView):

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            return None

    # GET /detail/<id>/
    def get(self, request, pk):
        item = self.get_object(pk)
        if item is None:
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    # PUT /edit/<id>/
    def put(self, request, pk):
        item = self.get_object(pk)
        if item is None:
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Item updated successfully.', 'data': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE /delete/<id>/
    def delete(self, request, pk):
        item = self.get_object(pk)
        if item is None:
            return Response({'error': 'Item not found.'}, status=status.HTTP_404_NOT_FOUND)
        item.delete()
        return Response({'message': 'Item deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    
class DeleteAllItemsView(APIView):
    def delete(self, request):
        Item.objects.all().delete()
        return Response({"message": "🗑️ All items deleted successfully!"})