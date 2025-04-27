from django.db import models

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    intuito = models.TextField()

    def __str__(self):
        return self.nome
