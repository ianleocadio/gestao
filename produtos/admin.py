from django.contrib import admin
from .models import Produto
# Register your models here.

class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "descricao", "preco")
    search_fields = ("id", "descricao")


admin.site.register(Produto, ProdutoAdmin)
