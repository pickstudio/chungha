from django.db import models
from .card import Card


class Benefit(models.Model):
    contents = models.CharField()
    card_id = models.ManyToManyField(Card)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)