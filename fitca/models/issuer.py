# 카드 발급사

from django.db import models
from enum import Enum


class Issuer(models.Model):
    # 카드사별로 코드가 있음 (002) 등
    code = models.CharField(max_length=12, unique=True)
    # '카드' 를 제외한 이름 KB국민(o) KB국민카드(x)
    name = models.CharField(null=False)
    name_eng = models.CharField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

