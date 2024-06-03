
from django.urls import path, include
from . import views



urlpatterns = [
    path('users', views.users, name='get_users'),
    path('users', views.users, name='create_user'),
    path('users/<int:email>', views.users, name='update_user'),
    path('users/<int:email>', views.users, name='get_user_by_id'),
    path('users/<int:email>', views.users, name='delete_user'),
]
