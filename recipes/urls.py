from django.urls import path
from .views import RecipeListCreateView, RecipeDetailView, RecipeByIngredientView

urlpatterns = [
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipes/ingredient/<str:ingredient>/', RecipeByIngredientView.as_view(), name='recipe-by-ingredient'),
]
