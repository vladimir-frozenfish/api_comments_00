from django.urls import path, include

from rest_framework import routers

from .views import CommentViewSet, PostViewSet

app_name = 'api'

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
# router.register('groups', GroupViewSet)
router.register(
     r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
 )
# router.register('follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
