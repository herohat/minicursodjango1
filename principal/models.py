from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
# from django.contrib.auth.models import User

# Ciudades.objects - Manager

class MyUserManager(BaseUserManager): # create_user - create_superuser
	def _create_user(self, email, dni, password, is_staff, is_superuser, **extra_fields):
		if not email:
			raise ValueError('El email debe ingresarse')
		email = self.normalize_email(email)
		user = self.model(email=email, dni=dni, is_active=True, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_user(self, email, dni, password=None, **extra_fields):
		return self._create_user(email, dni, password, False, False, **extra_fields)

	def create_superuser(self, email, dni, password, **extra_fields):
		return self._create_user(email, dni, password, True, True, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):
	email = models.EmailField(unique=True)
	dni = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=250)
	apellidos = models.CharField(max_length=250)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = MyUserManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['dni']