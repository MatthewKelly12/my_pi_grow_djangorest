from django.urls import path, include
from . import views 
from rest_framework import routers
from .views import TypeView

router = routers.DefaultRouter()
router.register('types', views.TypeView)


urlpatterns = [
    path('', include(router.urls))
]