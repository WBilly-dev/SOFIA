from django import forms
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
   
    
class Contenidos(models.Model):
    nombre=models.CharField(max_length=50)
    comentario=models.CharField(max_length=100)
    upload=models.FileField(upload_to='SofiaApp/static/SofiaApp/contenido' ,max_length=80)
    
    class Meta:
        permissions = [
            ("contenidoCR", "CreaContenidos"),
            ("contenidoMO", "ModificaContenidos"),
            ("contenidoDE", "EliminaContenidos"),
        ]
    
    
    def __str__(self):
        return self.nombre
    
class Tareas(models.Model):
    nombre=models.CharField(max_length=20)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    comentario=models.CharField(max_length=50)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)
    Contenido=models.ForeignKey(Contenidos,on_delete=models.CASCADE)
    
    class Meta:
        permissions = [
            ("CR_Tareas", "Posibilita Crear Tareas"),
            ("MO_Tareas", "Posibilita Modificar Tareas"),
            ("DE_Tareas", "Posibilita Eliminar Tareas"),
        ]
    def __str__(self):
        return self.nombre
                                
class Notas(models.Model):
    nombre=models.CharField(max_length=20)
    nota=models.IntegerField()
    comentario=models.CharField(max_length=50)
    Tarea=models.ForeignKey(Tareas,on_delete=models.CASCADE)
    usuario=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
    
    def validar_datos(self):
        # Verificar que el nombre no esté vacío
        if not self.nombre:
            return False

        # Verificar que la nota sea un número válido
        if not isinstance(self.nota, int) or self.nota < 0 or self.nota > 10:
            return False

        # Verificar que el comentario no esté vacío
        if not self.comentario:
            return False

        # Si todas las verificaciones pasan, los datos son válidos
        return True
    
    class Meta:
        permissions = [
            ("CR_Notas", "Posibilita Crear Notas"),
            ("MO_Notas", "Posibilita Modificar Notas"),
            ("DE_Notas", "Posibilita Eliminar Notas"),
        ]  
class Recurso_Educativos(models.Model):
    Autor=models.CharField(max_length=15)
    Nombre=models.CharField(max_length=100)
    upload=models.FileField(upload_to='recurso_educativo/')    
    Contenido=models.ForeignKey(Contenidos,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.Nombre   
    
    class Meta:
        permissions = [
            ("CR_Recurso", "Posibilita Crear Recursos"),
            ("MO_Recurso", "Posibilita Modificar Recursos"),
            ("DE_Recurso", "Posibilita Eliminar Recursos"),
        ]