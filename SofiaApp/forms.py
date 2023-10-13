from django.forms import *
from SofiaApp.models import Contenidos, Tareas , Recurso_Educativos , Notas 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class form_Contenidos(ModelForm):
    class Meta:
        model=Contenidos
        fields='__all__'
        
class form_Tareas(ModelForm):
    class Meta:
        model=Tareas
        fields='__all__'

class form_Recurso_Educativo(ModelForm):
    class Meta:
        model=Recurso_Educativos
        fields='__all__'

class form_Notas(ModelForm):
    class Meta:
        model=Notas
        fields='__all__'

   
        
        
class registroForm(UserCreationForm):            
                                
        class Meta :
            model=User
            fields=[
                'username',
                'first_name',
                'last_name',
                'email',
                
               
            ]
            labels={
                'username': 'Nombre de Usuario',
                'first_name': 'Nombre',
                'last_name':'Apellidos',
                'email':'Correo',
                
            }