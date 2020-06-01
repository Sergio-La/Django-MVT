from rest_framework import serializers
from .models import estudiante
from .models import profesor
from .models import materia
from .models import salones

#Serializador para estudiante
class estudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = estudiante
        fields = (
            'id',
            'est_cod',
            'est_nom',
            'est_ap',
            'est_cur',
        )

#Serializador para profesores
class profesorSerializer(serializers.ModelSerializer):
    class Meta:
        model = profesor
        fields = (
           'id',
           'pro_cod',
           'pro_nom',
           'pro_ap',
           'pro_are', 
        )

#Serializador para materias
class materiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = materia
        fields = (
           'id',
           'ma_cod',
           'ma_nom', 
        )

#Serializador para salones
class salonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = salones
        fields = (
           'id',
           'sal_cod',
           'sal_nom',
           'sal_cur', 
        )        