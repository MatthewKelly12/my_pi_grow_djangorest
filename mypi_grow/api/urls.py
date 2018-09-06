from django.urls import path, include
from . import views
from rest_framework import routers
from .views import TypeView, CategoryView, VarietyView, ConditionView

router = routers.DefaultRouter()
router.register('types', views.TypeView)
router.register('categories', views.CategoryView)
router.register('varieties', views.VarietyView)
router.register('conditions', views.ConditionView)


urlpatterns = [
    path('', include(router.urls))
]