from django.db import models
from atracoes.models import Atracoes
from avaliations.models import Avaliacoes
from comments.models import Comentarios
from localization.models import Enderecos

class PontosTuristicos(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    approved = models.BooleanField(default=False)
    attractions = models.ManyToManyField(Atracoes)
    comments = models.ManyToManyField(Comentarios)
    assessments = models.ManyToManyField(Avaliacoes)
    address = models.ForeignKey(Enderecos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
