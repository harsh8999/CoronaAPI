from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

# Create your models here.

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class Hospital(models.Model):
  name = models.CharField(max_length=200)
  address = models.TextField(max_length=500)
  city = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=200)

  def __str__(self):
    return self.name


class DocumentRegistration(models.Model):
  registationDate = models.DateTimeField(auto_now_add=True)
  name = models.CharField(max_length=100)
  date_of_birth = models.CharField(max_length=100)
  gender = models.CharField(max_length=10)
  phone = models.IntegerField(null=True, blank=True)
  id_card_type = models.CharField(max_length=100)
  id_card_number = models.IntegerField()
  address = models.TextField()
  city = models.CharField(max_length=50)
  state = models.CharField(max_length=100)
  eligible_for_vaccine = models.BooleanField(default=False)

  def __str__(self):
    return self.name
