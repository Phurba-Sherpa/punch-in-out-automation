
from django.urls import path, include
from . import views



urlpatterns = [
    path('users', views.users, name='get_users'),
    path('users', views.users, name='create_user'),
    path('users/<str:email>', views.user, name='update_user'),
    path('users/<str:email>', views.user, name='get_user_by_id'),
    path('users/<str:email>', views.user, name='delete_user'),
]
