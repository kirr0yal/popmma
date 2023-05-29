from django.urls import path

from main.views import *
from main.views_auth import *

urlpatterns = [
    path('', post_list, name='home'),
    path('tags/<tag>/<str:slug>', show_post_tags, name='tags'),
    path('login/', login_view, name='login'),
    path('tags/<str:tag>', show_tags_related_posts, name='show_tags_related_posts'),
    path('logout/', logout_view, name='logout'),
    path('login/', login_view, name='login'),
]

