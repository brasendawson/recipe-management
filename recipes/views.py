from django.db.models import Q
from rest_framework import generics, permissions
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Recipe
from .serializers import RecipeSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.views import APIView

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'category', 'ingredients']
    ordering_fields = ['prep_time', 'cook_time', 'servings']

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_update(self, serializer):
        if self.get_object().creator != self.request.user:
            raise permissions.PermissionDenied("You cannot edit someone else's recipe.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.creator != self.request.user:
            raise permissions.PermissionDenied("You cannot delete someone else's recipe.")
        instance.delete()

class RecipeByIngredientView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request, ingredient):
        recipes = Recipe.objects.filter(ingredients__icontains=ingredient)
        serializer = RecipeSerializer(recipes, many=True)
        return Response(serializer.data)