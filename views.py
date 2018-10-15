from rest_framework import viewsets
from clothes.models import Clothes
from clothes.serializers import ClothesSerializer

class ClothesViewSet(viewsets.ModelViewSet):

    model = Clothes
    queryset = Clothes.objects.all()
    serializer_class = ClothesSerializer
