from rest_framework import serializers
from .models import Recipe

class RecipeSerializer(serializers.ModelSerializer):
    creator = serializers.ReadOnlyField(source='creator.username')

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'description', 'ingredients', 'instructions',
            'category', 'prep_time', 'cook_time', 'servings',
            'created_date', 'creator'
        ]
