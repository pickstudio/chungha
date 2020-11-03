# 카드별 혜택 -> 단순히 카드가 가지고 있는 헤택을 나열할 것임

from django.db import models
from .card import Card


class Benefit(models.Model):
    contents = models.CharField()
    card_id = models.ManyToManyField(Card)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)