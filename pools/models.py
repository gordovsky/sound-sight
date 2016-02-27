from django.db import models
from django.utils import timezone
# from django.contrib.auth.models import AbstractBaseUser


class Point(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=30)
    description = models.TextField()
    created_date = timezone.now
    latitude = models.FloatField('Latitude')
    longitude = models.FloatField('Longitude')

    def __str__(self):
        return self.title


# class Account(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     username = models.CharField(max_length=30, unique=True)
#     first_name = models.CharField(max_length=30, blank=True)
#     last_name = models.CharField(max_length=30, blank=True)
#     tagline = models.CharField(max_length=100, blank=True)
#
#     is_admin = models.BooleanField(default=False)
#
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#
#     objects = AccountManager()
#
#     USERNAME_FIELD = 'username'
#     REQUIRED_FIELDS = ['username']
#
#     def __unicode__(self):
#         return self.email
#
#     def get_full_name(self):
#         return ' '.join([self.first_name, self.last_name])
#
#     def get_short_name(self):
#         return self.first_name
