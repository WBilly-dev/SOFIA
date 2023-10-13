from django.contrib import admin
from SofiaApp.models import Contenidos,Notas,Recurso_Educativos,Tareas

class tareaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

# Register your models here.
admin.site.register(Contenidos)
admin.site.register(Notas)
admin.site.register(Recurso_Educativos)
admin.site.register(Tareas,tareaAdmin)