from django.db import models
from django.utils import timezone

class Produto(models.Model):
    descricao = models.CharField(max_length=50,blank=False,null=False)
    preco = models.FloatField(max_length=50,blank=False,null=False)
    imagem = models.ImageField(blank=True,upload_to='imagens/')
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name = 'produto'
        verbose_name_plural = 'produtos'

    def __str__(self):
        return self.descricao
