from rest_framework.routers import DefaultRouter
from django.urls import include, path

from core.api.post.view import (
    PostViewset,
)


router = DefaultRouter()
router.register(
    r'post',
    PostViewset,
    basename='post'
)

urlpatterns = [
    path('api/', include(router.urls)),
]
