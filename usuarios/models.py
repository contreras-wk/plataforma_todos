from django.db import models
from django.contrib.auth.models import AbstractUser

from usuarios.managers import UsuarioManager


class Usuario(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UsuarioManager()
