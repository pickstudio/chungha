# 회원

from django.db import models
from enum import Enum


class Member(models.Model):
    class AUTH(Enum):
        ADMIN = 'admin'
        NORMAL = 'normal'

    code = models.CharField(max_length=12, unique=True)
    name = models.CharField(max_length=12, default='', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



