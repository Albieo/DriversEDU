from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class Role(models.Model):
    LICENCE_TYPE_CHOICES = (
        ('Learner', 'Learners Licence Student'),
        ('Driver', 'Drivers Licence Student'),
    )

    LICENCE_CODE_CHOICES = (
        ('', 'Licence Codes'),
        (1, 'Code A'),
        (2, 'Code B'),
        (3, 'Code C'),
        (4, 'Code E'),
    )

    licence_type = models.CharField(max_length=50, choices=LICENCE_TYPE_CHOICES)
    licence_code = models.IntegerField(choices=LICENCE_CODE_CHOICES)


class User(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=250)
    role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True, blank=True)

    groups = models.ManyToManyField(
        Group,
        related_name='k53_user_groups',
        blank=True,
        help_text='The groups this user belongs to.'
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='k53_user_permissions',
        blank=True,
        help_text='Specific permissions for this user.'
    )
