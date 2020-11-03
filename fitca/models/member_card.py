# 회원이 소지하고 있는 카드

from django.db import models
from .member import Member
from .card import Card


class MemberCard(models.Model):
    member = models.ForeignKey(Member)
    card = models.ForeignKey(Card)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)