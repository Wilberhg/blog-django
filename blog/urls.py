from django.urls import path
from blog.views import PostListView, post_detail

app_name = 'blog'

urlpatterns = [
    # views de postagens
    # path('', post_list, name='post_list'),
    path('', PostListView.as_view(), name='post_list'),
    path(
        '<int:year>/<int:month>/<int:day>/<slug:post>/',
        post_detail,
        name='post_detail'
    ),
]