from django.urls import path
from .views import home, RecipeDetailView, RecipeListView, add_recipe, about

# Create Url below
app_name = 'recipes'

urlpatterns = [
   path("", home, name="recipes_home"),
   path("recipes/", RecipeListView.as_view(), name="recipes_list"),
   path("recipes/<pk>/", RecipeDetailView.as_view(), name="recipes_detail"),
   path("add/", add_recipe, name="recipes_add"),
   path("about/", about, name="about"),
]