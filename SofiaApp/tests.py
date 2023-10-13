import time
from django.test import Client, TestCase

# Create your tests here.
from django.test import TestCase


from .forms import registroForm
from django.urls import reverse
from django.contrib.auth.models import User , Group
from .models import Notas, Recurso_Educativos, Tareas, Contenidos
from django.core.files.uploadedfile import SimpleUploadedFile
    


'''
#Ejemplo correcto de registro de usuario mediante un formulario
class registroFormTestCase(TestCase):
    def test_valid_form(self):
        # Crear datos de formulario válidos
        form_data = {
            'username': 'williamgf',
            'first_name': 'William',
            'last_name': 'Gomez',
            'email': 'williamgomezfernandez3@gmail.com',
            'password1': 'bHKcYWv4',
            'password2': 'bHKcYWv4'
        }
        # Crear una instancia del formulario con los datos
        form = registroForm(data=form_data)
        # Verificar que el formulario es válido
        self.assertTrue(form.is_valid())




#Ejemplo incorrecto de para comprobar la vista en una plantilla
class MyViewTestCase(TestCase):
    def test_my_view(self):
        # Obtener la URL de la vista utilizando `reverse`
        url = reverse('Home')
        # Realizar una solicitud GET a la URL
        response = self.client.get(url)
        # Verificar que la respuesta tiene un código de estado 200 (éxito)
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se utilizó para renderizar la respuesta
        self.assertTemplateUsed(response, 'index.html')
       
       
       
       
 
#Ejemplo correcto para comprobar la vista de plantilla       
    
class MyViewTestCaseCorrecto(TestCase):
    def test_my_view(self):
        # Obtener la URL de la vista utilizando `reverse`
        url = reverse('Home')
        # Realizar una solicitud GET a la URL
        response = self.client.get(url)
        # Verificar que la respuesta tiene un código de estado 200 (éxito)
        self.assertEqual(response.status_code, 200)
        # Verificar que la plantilla correcta se utilizó para renderizar la respuesta
        self.assertTemplateUsed(response, 'SofiaApp/index.html')        

       

        
#Ejemplo incorrecto de creacion de una tarea con llave foranea de dos modelos        
class TareasTestCase(TestCase):
    def setUp(self):
        # Crear un usuario y un contenido para usar en la prueba
        self.user = User.objects.create(username='testuser')
        self.contenido = Contenidos.objects.create(
            nombre='Test Contenido',
            comentario='Test Comentario',
            upload=SimpleUploadedFile('test.txt', b'Test Contenido')
        )
        
    def test_create_tarea(self):
        # Crear una tarea
        tarea = Tareas.objects.create(
            nombre='Test Tarea',
            comentario='Test Comentario',
            usuario=self.user,
            Contenido=self.contenido
        )
        # Verificar que la tarea se ha creado correctamente
        self.assertEqual(tarea.nombre, 'Test Tarea')
        self.assertEqual(tarea.comentario, 'Test Comentarios')   
 
 
#Ejemplo correcto de creacion de un contenido        
class testcontenido (TestCase):
    
    def test_create_contenido (self):
        contenido=Contenidos.objects.create(
            nombre='Test_Contenido',
            comentario='Test_Comentarios',
            upload=SimpleUploadedFile('test.txt',b'Test_Contenido')
        )
        #Verifica que el contenido se a creado correctamente
        self.assertEqual(contenido.nombre, 'Test_Contenido')
        self.assertEqual(contenido.comentario, 'Test_Comentarios')
        
        
#Ejemplo incorrecto de creacion de un Recurso Educativo
class testRE (TestCase):
    
    def setUp(self):
         self.contenido = Contenidos.objects.create(
            nombre='Test Contenido',
            comentario='Test Comentario',
            upload=SimpleUploadedFile('test.txt', b'Test Contenido')
         )
    
    def test_create_RE(self):
        RE=Recurso_Educativos.objects.create(
            Autor='William',
            Nombre='Turing',
            upload=SimpleUploadedFile('test.txt' , b'Test_Recurso'),
            Contenido=self.contenido
        )
        
        self.assertEqual(RE.Autor, 'Adrian')
        self.assertEqual(RE.Nombre, 'Turing')    
    


#Ejemplo incorrecto de la creacion de una Nota 
class testNota (TestCase):
    
    def setUp(self):
        self.contenido = Contenidos.objects.create(
            nombre='Test Contenido',
            comentario='Test Comentario',
            upload=SimpleUploadedFile('test.txt', b'Test Contenido')
        )
        self.user = User.objects.create(username='testuser')
        self.Tarea=Tareas.objects.create(
            nombre='Test Tarea',
            comentario='Test Comentario',
            usuario=self.user,
            Contenido=self.contenido
        )

    def test_create_Nota(self):
        Nota=Notas.objects.create(
            nombre='Turing',
            nota=5,
            comentario='Test_Nota',
            Tarea=self.Tarea,
            usuario=self.user                    
        )
        self.assertEqual(Nota.nombre, 'William')
 
 
 
 #Test correcto para comprobar la verificacion de redireccion con el status code 302 y la creacion de un nuevo contenido con permisos y su existencia en la base de datos
class ContenidosViewTest(TestCase):
     
    def test_crear_contenido_view(self):
        url = reverse('create_contenido')
        data = {
            'nombre': 'Nuevo Contenido',
            'comentario': 'Comentario del nuevo contenido',
            # Aquí se debe proporcionar un archivo válido para el campo 'upload'
            'upload':SimpleUploadedFile('test.txt',b'Test_Contenido')
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302) # Verifica que la vista redirige después de crear el contenido
        # Verifica que no se creó un nuevo objeto Contenidos en la base de datos porque la creacion de contenidos requiere permisos especiales
        self.assertFalse(Contenidos.objects.filter(nombre='Nuevo contenido').exists()) 
   
   
   
        
#Test para comprobar que un usario no tiene permiso para eliminar un recurso educativo
class DeleteRecursoViewTest(TestCase):
    def setUp(self):
        # Crear un usuario sin el permiso 'DE_recurso'
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.client.login(username='testuser', password='testpass')

    def test_delete_recurso_view_requires_permission(self):
        # Obtén la URL de la vista delete_Recurso
        url = reverse('delete_recurso', args=[1]) 
        response = self.client.get(url)
        # Verifica que la vista no permita el acceso al usuario sin el permiso 'DE_recurso'
        self.assertNotEqual(response.status_code, 403) # 403 Forbidden         




#Tests  donde se comprueba que el usuario pertenezca al grupo Admins y cree un nuevo usuario que es agregado al grupo Profesor
class CreateProfessorViewTestCase(TestCase):
    def setUp(self):
        # Crear un usuario que pertenece al grupo "Admins"
        self.admin_user = User.objects.create_user(username='admin', password='password')
        self.admin_group = Group.objects.create(name='Admins')
        self.admin_user.groups.add(self.admin_group)

        # Crear un usuario que no pertenece al grupo "Admins"
        self.non_admin_user = User.objects.create_user(username='non_admin', password='password')

        # Crear el grupo "Profesor"
        self.professor_group = Group.objects.create(name='Profesor')

        # Inicializar el cliente de prueba
        self.client = Client()



    def test_admin_user_can_access_view(self):
        # Iniciar sesión como el usuario que es parte del grupo "Admins"
        self.client.login(username='admin', password='password')

        # Intentar acceder a la vista `CreateProfessorView`
        response = self.client.get(reverse('create_professor'))

        # Verificar que el usuario puede acceder a la vista y ver el formulario
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views/create_professor.html')

    def test_create_new_user(self):
        # Iniciar sesión como el usuario que es parte del grupo "Admins"
        self.client.login(username='admin', password='password')

        # Enviar el formulario con datos válidos para crear un nuevo usuario
        response = self.client.post(reverse('create_professor'), {
            'first_name': 'First',
            'last_name': 'Last',
            'username': 'new_user',
            'email': 'new_user@example.com',
            'password1': 'password'
        })

        # Verificar que se ha creado un nuevo usuario con la información proporcionada
        new_user = User.objects.get(username='new_user')
        self.assertEqual(new_user.first_name, 'First')
        self.assertEqual(new_user.last_name, 'Last')
        self.assertEqual(new_user.email, 'new_user@example.com')

        # Verificar que el nuevo usuario ha sido agregado al grupo "Profesor"
        self.assertFalse(new_user.groups.filter(name='Profesor').exists())

    def test_redirect_after_creating_new_user(self):
        # Iniciar sesión como el usuario que es parte del grupo "Admins"
        self.client.login(username='admin', password='password')

        # Enviar el formulario con datos válidos para crear un nuevo usuario
        response = self.client.post(reverse('create_professor'), {
            'first_name': 'First',
            'last_name': 'Last',
            'username': 'new_user',
            'email': 'new_user@example.com',
            'password1': 'password'
        })

        # Verificar que después de crear un nuevo usuario, el usuario es redirigido a la página "login"
        self.assertRedirects(response, reverse('login'))

'''

#ISWII
class NotasTestCase(TestCase):
    def test_validar_datos_nota(self):
        # Crear una nota con datos válidos
        nota = Notas(nombre="Nota 1", nota=5, comentario="Comentario 1")
        self.assertTrue(nota.validar_datos())

        # Crear una nota con datos inválidos
        nota = Notas(nombre="", nota=5, comentario="Comentario 1")
        self.assertFalse(nota.validar_datos())
        
        print('La prueba test_validar_datos_nota se ejecutó correctamente')


class ListarContenidoTestCase(TestCase):
    def setUp(self):
        Contenidos.objects.create(nombre="Contenido 1", comentario="Comentario 1")
        Contenidos.objects.create(nombre="Contenido 2", comentario="Comentario 2")

    def test_listar_contenido(self):
        response = self.client.get('/list_contenido')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Contenido 1")
        self.assertContains(response, "Contenido 2") 
                
        print('La prueba de integración a la Base de Datos se ejecuto correctamente')
        
        
class NotasTestCase3(TestCase):
    def test_tiempo_de_respuesta_crear_nota(self):
        # Crear una nota con datos válidos
        start_time = time.time()
        response = self.client.post(reverse('create_nota'), {
            'nombre': 'Nota 1',
            'nota': 5,
            'comentario': 'Comentario 1'
        })
        end_time = time.time()

        # Calcular el tiempo de respuesta
        response_time = end_time - start_time
        
        # Mostrar el tiempo de respuesta en la consola
        

        # Verificar que el tiempo de respuesta sea inferior a un valor determinado
        self.assertLess(response_time, 1) # 1 segundo        
        print(f'Tiempo de respuesta de la creacion de notas es: {response_time:.2f} segundos')
        print('La prueba test_tiempo_de_respuesta_crear_nota se ejecutó correctamente')
        

class SeguridadTestCase(TestCase):
    def setUp(self):
        # Crear un usuario de prueba
        self.usuario = User.objects.create_user(username='usuario', password='password')

    def test_acceso_denegado(self):
        # Iniciar sesión como el usuario de prueba
        self.client.login(username='usuario', password='password')

        # Intentar acceder a una sección restringida
        response = self.client.get(reverse('create_contenido'))

        # Verificar que el sistema muestre un error 403 Forbidden
        self.assertEqual(response.status_code, 403)
        
        print('La prueba test_acceso_denegado se ejecutó correctamente')