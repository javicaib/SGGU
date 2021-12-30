from django.db import models
from django.contrib.auth.models import User

# Create your models here.
FAC_CHOICES = [
    (1, 'Facultad 1'),
    (2, 'Facultad 2'),
    (3, 'Facultad 3'),
    (4, 'Facultad 4'),
    (5, 'FTE'),
    (6, 'CITEC')
]
GROUP_CHOICES = [
    (1, 'F1401'),
    (2, 'F1402'),
    (3, 'F1403'),
    (4, 'F1404'),
    (5, 'F1405')
]


class Estudiante(User):
    facultad = models.CharField(choices=FAC_CHOICES, max_length=20)
    grupo = models.CharField(choices=GROUP_CHOICES, max_length=20)
