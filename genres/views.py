from rest_framework import filters, status, viewsets
from rest_framework.response import Response

from api.permissions import IsAdminOrStaff, ReadOnly

from .models import Genre
from .serializers import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [ReadOnly | IsAdminOrStaff]
    lookup_field = 'slug'
    filter_backends = [filters.SearchFilter]
    search_fields = ('=name',)
    http_method_names = ["get", "post", "delete"]

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
