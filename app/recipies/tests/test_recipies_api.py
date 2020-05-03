from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe, Tag, Ingredient

from recipies.serializer import RecipeSerializer, RecipeDetailSerializer

RECIPES_URL = reverse('recipies:recipe-list')


def dummy_recipe(user, **params):
    """Creates a dummy recipe"""
    defaults = {
        'title': 'power puff girls',
        'time_minutes': 1,
        'price': 500.00,
    }
    defaults.update(params)

    return Recipe.objects.create(user=user, **defaults)

def dummy_tag(user, name='Indian'):
    """Creates an example tag"""
    return Tag.objects.create(user=user, name=name)


def dummy_ingredient(user, name='beef'):
    """Creates ans  return a dummy ingredient"""
    return Ingredient.objects.create(user=user, name=name)


def detail_url(recipe_id):
    """returns the recipe detail URL"""
    return reverse('recipies:recipe-detail', args=[recipe_id])    


class PublicRecipeApiTests(TestCase):
    """unauthenticated API access testing"""

    def setUp(self):
        self.client = APIClient()

    def test_required_auth(self):
        """Test the authenticaiton is required"""
        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeApiTests(TestCase):
    """Test authenticated recipe API access"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@thanos.com',
            'invetible'
        )
        self.client.force_authenticate(self.user)


    def test_recipes_limited_to_user(self):
        """Test fetching recipes for user"""
        user2 = get_user_model().objects.create_user(
            'denvers@thor.com',
            'bringmethanos'
        )
        dummy_recipe(user=user2)
        dummy_recipe(user=self.user)

        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)


    def test_fetching_recipes(self):

        """Test fetching list of recipes"""
        dummy_recipe(user=self.user)
        
        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_view_recipe_detail(self):
        """Testing viewing a recipe detail"""
        recipe = dummy_recipe(user=self.user)
        recipe.tags.add(dummy_tag(user=self.user))
        recipe.ingredients.add(dummy_ingredient(user=self.user))

        url = detail_url(recipe.id)
        res = self.client.get(url)

        serializer = RecipeDetailSerializer(recipe)
        self.assertEqual(res.data, serializer.data)

    
    def test_create_basic_recipe(self):
        """Testing create recipe feature"""
        payload = {
            'title': 'rice and curry',
            'time_minutes': 30,
             'price': 60.00,
            }
        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))


    def test_create_recipe_with_tags(self):
        """Test creating a recipe with tags"""
        tag1 = dummy_tag(user=self.user, name='Tag 1')
        tag2 = dummy_tag(user=self.user, name='Tag 2')
        payload = {
            'title': 'two tagged test recipie',
            'tags': [tag1.id, tag2.id],
            'time_minutes': 30,
            'price': 500.00
        }
        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        tags = recipe.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(tag1, tags)
        self.assertIn(tag2, tags)


    def test_create_recipe_with_ingredients(self):
        """Testing recipe with ingredients"""
        ingredient1 = dummy_ingredient(user=self.user, name='Ingredient 1')
        ingredient2 = dummy_ingredient(user=self.user, name='Ingredient 2')
        
        payload = {
            'title': 'chiken biriyani',
            'ingredients': [ingredient1.id, ingredient2.id],
            'time_minutes': 60,
            'price': 150.00
        }

        res = self.client.post(RECIPES_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
        self.assertIn(ingredient1, ingredients)
        self.assertIn(ingredient2, ingredients) 