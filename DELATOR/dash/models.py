from django.db import models

class Maquina(models.Model):
    nome_maquina = models.CharField(max_length=200, blank=False)
    descricao = models.TextField(max_length=500)

    def __str__(self):
       return self.nome_maquina