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
    (1, 'G-01'),
    (2, 'G-02'),
    (3, 'G-03'),
    (4, 'G-04'),
    (5, 'G-05')
]


class Estudiante(User):
    facultad = models.IntegerField(choices=FAC_CHOICES)
    grupo = models.IntegerField(choices=GROUP_CHOICES)
    cambiar_pass = models.BooleanField(default=False)
