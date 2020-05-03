from django.urls import path, include
from rest_framework.routers import DefaultRouter

from recipies import views


router = DefaultRouter()#manages different url from one
router.register('tags', views.TagViewSet)
router.register('ingredients', views.IngredientViewSet)
router.register('recipies', views.RecipeViewSet)

app_name = 'recipies'

urlpatterns = [
    path('', include(router.urls))
]
