from django.contrib.auth.models import (
    UserManager,
    AbstractBaseUser,
    PermissionsMixin
)

from django.db import models


class CustomUserManager(UserManager):
    def _save_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Invalid email address')
        
        email = self.normalize_email(email)
        User = self.model(email=email, **extra_fields)
        User.set_password(password)

        User = User.save(using=self._db)
        
        return User
    

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._save_user(email, password, **extra_fields)
    

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._save_user(email, password, **extra_fields)


class Role(models.Model):
    description = models.CharField(max_length=50)


    def __str__(self):
        return self.description


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, blank=False, null=False, unique=True)
    first_name = models.CharField(max_length=50, blank=True, null=True)
    last_name = models.CharField(max_length=50, blank=True, null=True)

    role = models.ManyToManyField(Role, blank=True, null=True)

    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        ordering = ['email', '-date_joined', '-updated_at']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    @property
    def get_full_name(self):
        return f'{self.first_name.capitalize()} {self.last_name.capitalize()}'
    
    def get_short_name(self):
        return self.first_name


    def __str__(self):
        return self.email


