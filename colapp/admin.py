from django.contrib import admin
from .models import estudiante, profesor, materia, salones

admin.site.register(estudiante)
admin.site.register(profesor)
admin.site.register(materia)
admin.site.register(salones)