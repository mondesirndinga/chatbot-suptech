from django.contrib.auth.models import AbstractUser
from django.db import models

class Formation(models.Model):
    TYPE_CHOICES = [
        ('licence', 'Licence'),
        ('mastere', 'Mastère'),
        ('ingenieur', 'Cycle Ingénieur'),
    ]

    DOMAINE_CHOICES = [
        ('informatique', 'Informatique'),
        ('gestion', 'Gestion'),
        ('telecom', 'Télécom'),
        ('droit', 'Droit'),
        ('autre', 'Autre'),
    ]

    nom = models.CharField(max_length=255)
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    domaine = models.CharField(max_length=50, choices=DOMAINE_CHOICES, default='autre')
    mots_cles = models.TextField(blank=True)
    debouches = models.TextField(blank=True)
    conditions_admission = models.TextField(blank=True)
    description = models.TextField(blank=True)
    ressources_pedagogiques = models.TextField(blank=True)

    def __str__(self):
        return self.nom


class ChatInteraction(models.Model):
    user_query = models.TextField()
    bot_response = models.TextField()
    intent = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Interaction du {self.created_at}"


class Resource(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    age = models.PositiveIntegerField(null=True, blank=True)
    current_class = models.CharField(max_length=100)
    formation = models.CharField(max_length=100)

    def __str__(self):
        return self.username
