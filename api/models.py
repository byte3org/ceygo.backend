from django.db import models
from django.contrib.auth.models import AbstractBaseUser

class User(AbstractBaseUser):
	username = models.CharField(max_length=20, unique=True)
	email = models.EmailField(unique=True)
	password = models.CharField(max_length=30)
	passport_number = models.CharField(max_length=9)
	passport_expiry_date = models.DateField()
	birthdate = models.DateField()
	country = models.CharField(max_length=30)
	passport_front_image = models.ImageField(null=True)
	passport_back_image = models.ImageField(null=True)
	face_image = models.ImageField(null=True)

	USERNAME_FIELD = "username"

	def __str__(self):
		return f"User ({self.username})"
	