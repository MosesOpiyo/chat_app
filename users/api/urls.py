from django.urls import path

from users.api import views as users_views
from rest_framework.authtoken import views


urlpatterns = [
    path('register',users_views.registration_view,name="register"),
    path('login',users_views.login_user,name="login"),
    path('delete/<int:pk>',users_views.delete_user,name="delete"),
]
