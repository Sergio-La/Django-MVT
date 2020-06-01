from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import estudiante, profesor, materia, salones

class estudianteForm(forms.ModelForm):
    class Meta:
        model = estudiante
        fields = ['est_cod', 'est_nom', 'est_ap', 'est_cur']

class profesorForm(forms.ModelForm):
    class Meta:
        model = profesor
        fields = [
            'pro_cod', 'pro_nom', 'pro_ap', 'pro_are'
        ]

class materiaForm(forms.ModelForm):
    class Meta:
        model = materia
        fields = [
            'ma_cod', 'ma_nom'
        ]

class salonesForm(forms.ModelForm):
    class Meta:
        model = salones
        fields = [
            'sal_cod', 'sal_nom', 'sal_cur'
        ]

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']