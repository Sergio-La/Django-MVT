from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from rest_framework import generics


from .models import estudiante, profesor, materia, salones
from .forms import estudianteForm, profesorForm, materiaForm, salonesForm, CreateUserForm

from .serializers import estudianteSerializer, profesorSerializer, materiaSerializer, salonesSerializer




class estudiantelist(generics.ListCreateAPIView):
    queryset = estudiante.objects.all()
    serializer_class = estudianteSerializer

class profesorlist(generics.ListCreateAPIView):
    queryset = profesor.objects.all()
    serializer_class = profesorSerializer

class materialist(generics.ListCreateAPIView):
    queryset = materia.objects.all()
    serializer_class = materiaSerializer

class saloneslist(generics.ListCreateAPIView):
    queryset = salones.objects.all()
    serializer_class = salonesSerializer

@login_required(login_url='login')
def Home(request):
    return render(request,'index.html')

@login_required(login_url='login')
def crearEstudiante(request):
    if request.method == 'POST':
        estudiante_form = estudianteForm(request.POST)
        if estudiante_form.is_valid():
            estudiante_form.save()
            return redirect('index')
    else:
        estudiante_form = estudianteForm()
    return render(request,'colapp/crear_estudiante.html',{'estudiante_form':estudiante_form})

@login_required(login_url='login')
def listarEstudiante(request):
    estudiantes = estudiante.objects.all()
    return render(request,'colapp/listar_estudiante.html',{'estudiantes':estudiantes})

@login_required(login_url='login')
def crearProfesor(request):
    if request.method == 'POST':
        profesor_form = profesorForm(request.POST)
        if profesor_form.is_valid():
            profesor_form.save()
            return redirect('index')
    else:
        profesor_form = profesorForm()
    return render(request,'colapp/crear_profesor.html',{'profesor_form':profesor_form})

@login_required(login_url='login')
def listarProfesor(request):
    profesores = profesor.objects.all()
    return render(request,'colapp/listar_profesor.html',{'profesores':profesores})

@login_required(login_url='login')
def crearMateria(request):
    if request.method == 'POST':
        materia_form = materiaForm(request.POST)
        if materia_form.is_valid():
            materia_form.save()
            return redirect('index')
    else:
        materia_form = materiaForm()
    return render(request,'colapp/crear_materia.html',{'materia_form':materia_form})

@login_required(login_url='login')
def listarMateria(request):
    materias = materia.objects.all()
    return render(request,'colapp/listar_materia.html',{'materias':materias})

@login_required(login_url='login')
def crearSalones(request):
    if request.method == 'POST':
        salones_form = salonesForm(request.POST)
        if salones_form.is_valid():
            salones_form.save()
            return redirect('index')
    else:
        salones_form = salonesForm()
    return render(request,'colapp/crear_salones.html',{'salones_form':salones_form})

@login_required(login_url='login')
def listarSalones(request):
    salon = salones.objects.all()
    return render(request,'colapp/listar_salones.html',{'salon':salon})

def regUsuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                messages.success(request, 'Esta cuenta fue creada por ' + user)
                form.save()
                return redirect ('login')

        context = {'form':form}
        return render(request, 'cuentas/registro.html', context)

def logUsuario(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.info(request, 'Nombre de usuario o contraseña incorrecta')
                
        context = {}
        return render(request, 'cuentas/login.html', context)

def logouUsuario(request):
    logout(request)
    return redirect('login')