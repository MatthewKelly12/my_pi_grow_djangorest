from django.urls import path, include
from . import views
from rest_framework import routers
from .views import TypeView, CategoryView, VarietyView, ConditionView, GrowView

router = routers.DefaultRouter()
router.register('types', views.TypeView)
router.register('categories', views.CategoryView)
router.register('varieties', views.VarietyView)
router.register('conditions', views.ConditionView)
router.register('grows', views.GrowView)
router.register('datasets', views.DatasetView)


urlpatterns = [
    path('', include(router.urls))
]