from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all().order_by('-created_at')
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(category__iexact=category)  # <-- ✅ correct filter
        return queryset
