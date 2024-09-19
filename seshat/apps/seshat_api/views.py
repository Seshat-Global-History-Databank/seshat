from django.http import HttpResponse, JsonResponse

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view

from ..core.models import Polity, Reference

from .serializers import (
    PolitySerializer,
    ReferenceSerializer,
)


class PolityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Polities to be viewed or edited.
    """

    queryset = Polity.objects.all()
    serializer_class = PolitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(["GET", "POST"])
def reference_list_view(request, format=None):
    """
    List all references, or create a new reference.
    """
    if request.method == "POST":
        serializer = ReferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "GET":
        refs = Reference.objects.all()
        serializer = ReferenceSerializer(refs, many=True)
        return JsonResponse(serializer.data, safe=False)


@api_view(["GET", "PUT", "DELETE"])
def reference_detail_view(request, pk, format=None):
    """
    Retrieve, update or delete a reference.
    """
    try:
        ref = Reference.objects.get(pk=pk)
    except Reference.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = ReferenceSerializer(ref)
        return JsonResponse(serializer.data)

    elif request.method == "PUT":
        serializer = ReferenceSerializer(ref, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        ref.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)
