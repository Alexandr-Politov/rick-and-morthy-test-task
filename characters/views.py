import random

from django.db.models import QuerySet
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from drf_spectacular.utils import extend_schema, OpenApiParameter

from characters.models import Character
from characters.serializers import CharacterSerializer
from pagination import CharactersListPagination


@extend_schema(responses={status.HTTP_200_OK: CharacterSerializer})
@api_view(["GET"])
def get_random_character(request: Request) -> Response:
    """Get random character from Rick and Morty world."""
    pks = Character.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    random_character = Character.objects.get(pk=random_pk)
    serializer = CharacterSerializer(random_character)
    return Response(serializer.data, status=status.HTTP_200_OK)


class CharacterListView(generics.ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    pagination_class = CharactersListPagination

    def get_queryset(self) -> QuerySet:
        """
        Optionally restricts the returned purchases to a given character,
        by filtering against a `name` query parameter in the URL.
        """
        queryset = super().get_queryset()
        name = self.request.query_params.get("name")
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @extend_schema(
        parameters=[
            OpenApiParameter(
                name="name",
                description="Filter characters by name (insensitive contains)",
                required=False,
                type=str,
            ),
        ]
    )
    def get(self, request, *args, **kwargs) -> Response:
        return super().get(request, *args, **kwargs)
