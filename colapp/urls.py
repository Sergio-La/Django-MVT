from django.urls import path
from .views import estudiantelist, profesorlist, materialist, saloneslist, crearEstudiante, listarEstudiante, listarProfesor, crearProfesor, crearMateria, listarMateria, crearSalones, listarSalones, logUsuario, regUsuario, Home, logouUsuario

urlpatterns = [
    path('estudiante/', estudiantelist.as_view(), name = 'estudiante_list'),
    path('profesor/', profesorlist.as_view(), name = 'profesor_list'),
    path('materia/', materialist.as_view(), name = 'materia_list'),
    path('salones/', saloneslist.as_view(), name = 'salones_list'),
    path('crear_estudiante/', crearEstudiante, name = "crear_estudiante"),
    path('listar_estudiante/', listarEstudiante, name = 'listar_estudiante'),
    path('listar_profesor/', listarProfesor, name = 'listar_profesor'),
    path('crear_profesor/', crearProfesor, name = 'crear_profesor'),
    path('crear_materia/', crearMateria, name = 'crear_materia'),
    path('listar_materia/', listarMateria, name = 'listar_materia'),
    path('crear_salones/', crearSalones, name = 'crear_salones'),
    path('listar_salones/', listarSalones, name = 'listar_salones'),
    path('login/', logUsuario, name = 'login'),
    path('logout/', logUsuario, name = 'logout'),
    path('registro/', regUsuario, name = 'registro'),
]