from django.db import models
from django.contrib.auth.models import AbstractUser

# Usuário personalizado com dados de perfil embutidos
class Usuario(AbstractUser):
    idade = models.IntegerField(null=True, blank=True)
    peso = models.FloatField(null=True, blank=True)
    altura = models.FloatField(null=True, blank=True)
    objetivo = models.CharField(max_length=100, null=True, blank=True)
    frequencia_treino = models.CharField(max_length=100, null=True, blank=True)
    nivel_condicionamento = models.CharField(max_length=100, null=True, blank=True)
    restricoes = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.username

class TreinoGerado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='treinos')
    treino_texto = models.TextField()
    data_geracao = models.DateTimeField(auto_now_add=True)
    modelo_usado = models.CharField(max_length=100)

    def __str__(self):
        return f'Treino de {self.usuario.username} em {self.data_geracao.strftime("%d/%m/%Y")}'

class Feedback(models.Model):
    treino = models.ForeignKey(TreinoGerado, on_delete=models.CASCADE, related_name='feedbacks')
    nota = models.IntegerField()
    comentario = models.TextField(blank=True, null=True)
    data_feedback = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Feedback para treino {self.treino.id}'
