from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Recipe

from recipies.serializer import RecipeSerializer


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