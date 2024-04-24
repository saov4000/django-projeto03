from django.db import models

class Produto(models.Model):
    descricao = models.CharField(max_length=50,blank=False,null=False)
    preco = models.FloatField(max_length=50,blank=False,null=False)
    estoque = models.IntegerField(max_length=50,blank=False,null=False)

    def __str__(self):
        return self.descricao
