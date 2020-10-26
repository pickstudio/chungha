from django.db import models
from enum import Enum
from .tag import Tag


class Card(models.Model):
    class BRAND(Enum):
        VISA = 'visa'
        MASTER = 'master'
        AMEX = 'american_express'
        UNIONPAY = 'union_pay'

    # belongs to issuer
    name = models.CharField()
    # 혜택 benefits
    # image
    # 브랜드 visa master amex
    tags = models.ManyToManyField(Tag)  # benefit categories 특징을 달 수 있다.
    opened_at = models.DateTimeField()  # 출시일
    closed_at = models.DateTimeField()  # 발매 중단일
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
