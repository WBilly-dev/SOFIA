from django.http import FileResponse, Http404 
from django.shortcuts import render, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,CreateView,DeleteView,UpdateView
from SofiaApp.forms import form_Contenidos , form_Recurso_Educativo , form_Tareas , form_Notas, registroForm 
from SofiaApp.models import Contenidos,Tareas,Notas,Recurso_Educativos
from django.contrib.auth.models import User , Group
from django.contrib.auth.forms import UserCreationForm
from rolepermissions.mixins import HasPermissionsMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import redirect



# Create your views here.
def home(request):
    return render(request, "SofiaApp/index.html")

def Iniciar_Sesion(request):
    return render(request, "SofiaApp/login.html")

def Registrarse(request):
    return render(request, "views/registrarse.html")

def Administrar_Contenido(request):
    return render(request, "SofiaApp/administrarContenido.html")

def Contenido(request):
    return render(request, "SofiaApp/contenido.html")

def Administrar_Nota(request):
    return render(request, "SofiaApp/administrarNota.html")

def Nota(request):
    return render(request, "SofiaApp/nota.html")

def Administrar_Recurso_Educativo(request):
    return render(request, "SofiaApp/administrarRecursoEducativo.html")

def Recurso_Educativo(request):
    return render(request, "SofiaApp/recursoEducativo.html")

def Administrar_Tarea(request):
    return render(request, "SofiaApp/administrarTarea.html")

def Tarea(request):
    return render(request, "SofiaApp/tarea.html")

def show_pdf1(request):
    try:
        return FileResponse(open('SofiaApp/contenido/conjuntos.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    
def show_pdf2(request):
    try:
        return FileResponse(open('SofiaApp/contenido/LM.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    
def show_pdf3(request):
    try:
        return FileResponse(open('SofiaApp/contenido/teoriadegrafos.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    
def show_pdf4(request):
    try:
        return FileResponse(open('SofiaApp/contenido/COMBINATORIA.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    
def show_pdf5(request):
    try:
        return FileResponse(open('SofiaApp/contenido/teoria de numeros.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    
    
def show_pdf6(request):
    try:
        return FileResponse(open('SofiaApp/contenido/teoria de codificacion.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
    
def show_pdf7(request):
    try:
        return FileResponse(open('SofiaApp/contenido/teoria de la informacion.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
def show_pdf8(request):
    try:
        return FileResponse(open('SofiaApp/contenido/teoria de juegos.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()
def show_pdf9(request):
    try:
        return FileResponse(open('SofiaApp/contenido/Criptografia.pdf', 'rb'), content_type='application/pdf')
    except FileNotFoundError:
        raise Http404()                                

class listar_contenidos(ListView):
    model=Contenidos
    template_name='views/listarcontenidos.html'
    queryset=Contenidos.objects.all()
    
class create_contenido(PermissionRequiredMixin, CreateView):
    permission_required ='contenidoCR'
    model = Contenidos
    template_name = 'views/crearcontenido.html'
    form_class = form_Contenidos
    success_url = reverse_lazy('list_contenido')
        
class delete_contenido(PermissionRequiredMixin,DeleteView):
    permission_required='contenidoDE'
    model=Contenidos
    template_name='views/deletecontenido.html'
    success_url=reverse_lazy('list_contenido') 
    
class update_contenido(PermissionRequiredMixin,UpdateView):
    permission_required='contenidoMO'
    model=Contenidos
    template_name='views/updatecontenido.html'
    form_class=form_Contenidos
    success_url=reverse_lazy('list_contenido')      
    
class listar_recurso(ListView):
    model=Recurso_Educativos
    template_name='views/listarrecurso.html'
    queryset=Recurso_Educativos.objects.all()
    
class crear_recurso(HasPermissionsMixin,CreateView):
    required_permission='CR_recurso'
    model=Recurso_Educativos
    template_name='views/createrecurso.html'
    form_class=form_Recurso_Educativo
    success_url=reverse_lazy('list_recurso')
    
class delete_Recurso(HasPermissionsMixin,DeleteView):
    required_permission='DE_recurso'
    model=Recurso_Educativos
    template_name='views/deleterecurso.html'
    success_url=reverse_lazy('list_recurso') 
    
class update_recurso(HasPermissionsMixin,UpdateView):
    required_permission='MO_contenido'
    model=Recurso_Educativos
    template_name='views/updaterecurso.html'
    form_class=form_Recurso_Educativo
    success_url=reverse_lazy('list_recurso')  
    

class listar_tarea(ListView):
    model=Tareas
    template_name='views/listartarea.html'
    
    def get_queryset(self):
        return Tareas.objects.filter(usuario=self.request.user)
    
class listar_tarea1(ListView):
    model=Tareas
    template_name='SofiaApp/tarea.html'
    
    
    def get_queryset(self):
        return Tareas.objects.filter(usuario=self.request.user)   
    
class crear_tarea(HasPermissionsMixin,CreateView):
    required_permission='CR_tarea'
    model=Tareas
    template_name='views/createtarea.html'
    form_class=form_Tareas
    success_url=reverse_lazy('list_tarea')
    
class delete_tarea(HasPermissionsMixin,DeleteView):
    required_permission='DE_contenido'
    model=Tareas
    template_name='views/deletetarea.html'
    success_url=reverse_lazy('list_tarea') 
    
class update_tarea(HasPermissionsMixin,UpdateView):
    required_permission='MO_tarea'
    model=Tareas
    template_name='views/updatetarea.html'
    form_class=form_Tareas
    success_url=reverse_lazy('list_tarea') 
    
    
class listar_nota(ListView):
    model=Notas
    template_name='views/listarnota.html'


    def get_queryset(self):
        return Notas.objects.filter(usuario=self.request.user)
class listar_nota1(ListView):
    model=Notas
    template_name='SofiaApp/nota.html'
 
    
    def get_queryset(self):
        return Notas.objects.filter(usuario=self.request.user)  
    
class crear_nota(HasPermissionsMixin,CreateView):
    required_permission='CR_nota'
    model=Notas
    template_name='views/createnota.html'
    form_class=form_Notas
    success_url=reverse_lazy('list_nota')
    
class delete_nota(HasPermissionsMixin,DeleteView):
    required_permission='DE_nota'
    model=Notas
    template_name='views/deletenota.html'
    success_url=reverse_lazy('list_nota') 
    
class update_nota(HasPermissionsMixin,UpdateView):
    required_permission='MO_nota'
    model=Notas
    template_name='views/updatenota.html'
    form_class=form_Notas
    success_url=reverse_lazy('list_nota')     
    
class registroUsuario(CreateView):
    model = User
    template_name = 'views/registrar.html'
    form_class = registroForm
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context

    def form_valid(self, form):
        response = super().form_valid(form)

    # Agregar al usuario al grupo "Estudiante"
        group = Group.objects.get(name='Estudiante')
        group.user_set.add(self.object)

        return response
    

def my_view(request):
    is_professor = request.user.groups.filter(name='Profesor').exists()
    context = {'is_professor': is_professor}
    return render(request, 'base.html', context)        



class CreateProfessorView(LoginRequiredMixin, View):
    def dispatch(self, request, *args, **kwargs):
        # Verificar si el usuario logueado pertenece al grupo "Admins"
        if not request.user.groups.filter(name='Admins').exists():
            # Si el usuario no pertenece al grupo "Admins", redirigirlo a otra página
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request):
        # Mostrar el formulario para crear un nuevo usuario
        return render(request, 'views/create_professor.html')

    def post(self, request):
        # Obtener los valores de los campos del formulario
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password1')

        # Crear un nuevo usuario con los valores del formulario
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=email,
            password=password
        )
        user.is_superuser = True
        user.save()

        # Agregar al usuario al grupo "Profesor"
        group = Group.objects.get(name='Profesor')
        user.groups.add(group)

        # Redirigir al usuario a otra página
        return redirect('login') 