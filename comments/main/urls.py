from django.urls import include, path
from rest_framework_swagger.views import get_swagger_view

from .routers import router_v1
from .views import CommentView, PostsView


schema = get_swagger_view('Comments API')

router_v1.register(
    'posts',
    PostsView,
    basename='posts'
)
router_v1.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentView,
    basename='comments'
)

urlpatterns = [
    path('api/v1/', include(router_v1.urls)),
    path('api/v1/doc/', schema)
]
