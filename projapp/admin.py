from django.contrib import admin
from .models import Produto

class ProdutoAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(Produto,ProdutoAdmin)

