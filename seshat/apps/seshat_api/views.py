from django.contrib.auth.models import User, Group
from django.http import HttpResponse, JsonResponse
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view

from ..core.models import Polity, Reference

from .serializers import (
    UserSerializer,
    GroupSerializer,
    PolitySerializer,
    ReferenceSerializer,
)


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PolityViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Politys to be viewed or edited.
    """

    queryset = Polity.objects.all()
    serializer_class = PolitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@api_view(["GET", "POST"])
def reference_list(request, format=None):
    """
    List all references, or create a new reference.
    """
    if request.method == "GET":
        refs = Reference.objects.all()
        serializer = ReferenceSerializer(refs, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == "POST":
        serializer = ReferenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
def reference_detail(request, pk, format=None):
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
