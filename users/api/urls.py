from django.urls import path

from users.api import views as account_views
from rest_framework.authtoken import views


urlpatterns = [
    path('register',account_views.registration_view,name="register"),
    path('login',account_views.login_user,name="login"),
    path('delete/<int:pk>',account_views.delete_user,name="delete"),
]
