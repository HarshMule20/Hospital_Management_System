from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

USER_TYPE = [
    ('1', 'Patient'),
    ('2', 'Doctor')
]

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female.')
]



class User(AbstractUser):
    user_type = models.CharField(max_length=1, choices=USER_TYPE)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "User"