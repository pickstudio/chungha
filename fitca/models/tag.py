# 혜택 카테고리들의 해쉬태그

from django.db import models


class Tag(models.Model):
    name = models.CharField(unique=True, null=False)
    name_eng = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)