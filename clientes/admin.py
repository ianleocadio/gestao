from django.contrib import admin
from .models import Person, Documento



class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ("Dados pessoiais", {"fields": ('first_name', "last_name", "doc")}),
        ("Dados complementares",{
            "classes": ("collapse",),
            "fields": ("age", "salary", "photo")
        })
    )
    list_filter = ("age", "salary")
    list_display = ("completeName", "doc", "age", "salary", "bio", "hasPhoto")
    search_fields = ["id", "first_name"]


    def hasPhoto(self, instance):
        if instance.photo:
            return "Sim"
        else:
            return "Não"
    hasPhoto.short_description = "Possui foto ?"

    def completeName(self, instance):
        return instance.first_name + " " + instance.last_name
    completeName.short_description = "nome"





admin.site.register(Person, PersonAdmin)
admin.site.register(Documento)




admin.site.site_header = "Gestão de Clientes"
admin.site.index_title = "Administração"
admin.site.site_title = "Seja bem vindo ao Gestão de Clientes"
