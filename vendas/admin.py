from django.contrib import admin
from .actions import nfe_emitida, nfe_nao_emitida
from .models import Venda, ItemDoPedido

# Register your models here.

class ItemPedidoInline(admin.TabularInline):
#class ItemPedidoInline(admin.StackedInline):
    model = ItemDoPedido
    extra = 1

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ("valor",)
    raw_id_fields = ("pessoa",)
    autocomplete_fields = ["pessoa"]
    list_filter = ("pessoa__doc", "desconto")
    inlines = [ItemPedidoInline]
    list_display = ("id", "pessoa", "nfe_emitida")
    search_fields = ("id", "pessoa__first_name", "pessoa__doc__num_doc")
    actions = [nfe_emitida, nfe_nao_emitida]
    #filter_horizontal = ["produtos"]

    def total(self, instance):
        return instance.get_total()

admin.site.register(Venda, VendaAdmin)
admin.site.register(ItemDoPedido)