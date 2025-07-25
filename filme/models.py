from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
# Create your models here.

LISTA_CATEGORIAS = (
  ("ANALISES", "Análises"),
  ("PROGRAMACAO", "Programação"),
  ("APRESENTACAO", "Apresentação"),
  ("OUTROS", "Outros"),
)

# Criar o filme
class Filme(models.Model):
  titulo = models.CharField(max_length=100)
  thumb = models.ImageField(upload_to='thumb-filmes')
  descricao = models.TextField(max_length=1023)
  categoria = models.CharField(max_length=50, choices=LISTA_CATEGORIAS)
  visualizacoes = models.IntegerField(default=0)
  data_criacao = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.titulo

# Criar os episódios
class Episodio(models.Model):
  filme = models.ForeignKey(Filme, related_name='episodios', on_delete=models.CASCADE)
  titulo = models.CharField(max_length=100)
  video = models.URLField()
  thumb = models.URLField(default="")

  def __str__(self):
    return self.filme.titulo + " - " + self.titulo

class Usuario(AbstractUser):
  filmes_vistos = models.ManyToManyField(Filme, related_name='filmes_vistos')

  def __str__(self):
    return self.username
