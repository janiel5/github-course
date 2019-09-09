from django.db import models

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    email = models.EmailField(max_length=100)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.name

# Create your models here.
