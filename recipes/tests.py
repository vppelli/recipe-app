from django.test import TestCase
from .models import Recipe
from .forms import RecipesSearchForm, RecipeAddForm

# Create your tests here.
class RecipeModuleTest(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods
        Recipe.objects.create(name='Tea', ingredients='Tea leaves, Sugar, Water', cooking_time=10, difficulty='Easy')
    
    def test_recipe_name(self):
        recipe = Recipe.objects.get(id=1)
        field_label = recipe._meta.get_field('name').verbose_name

        # Compare the value to the expected result
        self.assertEqual(field_label, 'name')
    
    def test_name_max_length(self):
        # Get a recipe object to test
        recipe = Recipe.objects.get(id=1)

        # Get the metadata for the 'name' field and use it to query its max_length
        max_length = recipe._meta.get_field('name').max_length

        # Compare the value to the expected result i.e. 120
        self.assertEqual(max_length, 200)

class RecipesSearchFormTest(TestCase):
    def test_form_data(self):
        form = RecipesSearchForm(data={"recipe_title": "Tea", "chart_type": "#2"})
        self.assertTrue(form.is_valid())

class RecipeAddFormTest(TestCase):
    def test_recipe_add_form(self):
        # Verifies that the form is valid with all fields correctly filled out.
        form_data = {
            'name': 'Chocolate Cake',
            'ingredients': 'Chocolate, Flour, Sugar, Eggs',
            'cooking_time': 45,
            'about': 'Delicious chocolate cake recipe',
            'pic': '',
        }
        form = RecipeAddForm(data=form_data)
        self.assertTrue(form.is_valid())

class RecipeViewsTest(TestCase):
    def test_login_required_for_list_view(self):
        # Checks if user enters /recipes/ and is not logged in to redirect to /login/ than back to /recipes/.
        response = self.client.get('/recipes/')
        self.assertRedirects(response, '/login/?next=/recipes/')

    def test_login_required_for_detail_view(self):
        # Checks if user enters /recipes/1/ and is not logged in to redirect to /login/ than back to /recipes/1/.
        response = self.client.get(f'/recipes/1/')
        self.assertRedirects(response, f'/login/?next=/recipes/1/')
    
    def test_home_page_status_code(self):
        # Verifies that the home page is accessible and returns the correct HTTP status code.
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)