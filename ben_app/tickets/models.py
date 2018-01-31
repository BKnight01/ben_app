from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Board(models.Model):
    count = models.IntegerField()


class Ticket(models.Model):
    CATEGORY_CHOICES = (('Severe', 'Severe'), ('Moderate', 'Moderate'), ('Minor', 'Minor'))
    STATUS_CHOICES = (('New', 'New'), ('Under Review', 'Under Review'), ('Solved', 'Solved'))

    board = models.ForeignKey(Board, on_delete=models.CASCADE, default=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, default="")
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default="")
    status = models.CharField(max_length=80, choices=STATUS_CHOICES, default="")
    description = models.TextField(default="")
    rating = models.IntegerField(default=1)

    # Are any methods actually required?

    # ToString method?
    def __str__(self):
        return self.title


@receiver(post_save, sender=Ticket)
def send_request(sender, **kwargs):
    if kwargs.get('created', False):
        board = kwargs['instance'].board
        board.count += 1    # Increments the board count by one.
        board.save()











