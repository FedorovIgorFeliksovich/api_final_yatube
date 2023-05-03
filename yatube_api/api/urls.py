from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import CommentViewSet, GroupViewSet, PostViewSet

# DefaulRouter, в отличии от SimpleRouter, генерирует корневой эндпоинт "/"
v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet)


urlpatterns = [
    path('api/v1/', include(v1_router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
