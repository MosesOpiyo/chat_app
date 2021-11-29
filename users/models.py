from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager,Group,PermissionsMixin
from django.db.models.deletion import CASCADE

class MyAccountManager(BaseUserManager):
    """defines the methods to manage the custom user to be created
    Args:
        BaseUserManager ([type]): [description]
    Returns:
        [type]: [description]
    """
    def create_user(self,email,username,password=None):
        if not email:
            raise ValueError("Users must have and email address")
        if not username:
            raise ValueError("Users must have a username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            password = password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,email,username,password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
        )

        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user
    
class Account(PermissionsMixin,AbstractBaseUser)
