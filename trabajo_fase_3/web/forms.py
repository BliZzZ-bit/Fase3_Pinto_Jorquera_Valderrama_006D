from django import forms
from . models import Autor, Receta

class AutorForm(forms.ModelForm):
    pnombre = forms.CharField(label='Nombre del autor',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    papellido = forms.CharField(label='Apellido del autor',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    fechanac = forms.DateField(label='Fecha de nacimiento', widget=forms.DateInput(
        attrs={
            'class':'form-control'
        }
    ))
    fechamuerte = forms.DateField(label='Fecha de defuncion', widget=forms.DateInput(
        attrs={
            'class':'form-control'
        }
    ))
    class Meta:
        model = Autor
        fields = ('pnombre', 'papellido', 'fechanac', 'fechamuerte',)

class RecetaForm(forms.ModelForm):
    titulo = forms.CharField(label='Nombre de la receta',max_length=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    receta = forms.Textarea(label='Preparación',max_length=3000, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    autor = forms.CharField(label='Nombre del autor', max_lenght=100, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))
    preparacion = forms.CharField(label='Tipo de receta',max_lenght=200, widget=forms.TextInput(
        attrs={
            'class':'form-control'
        }
    ))

    imagen = forms.ImageField(label='Imagen', widget=forms.ImageField(
        attrs={
            'class':'form-control'
        }
    ))

    fechingreso = forms.DateField(label='Fecha de ingreso', widget=forms.DateInput(
        attrs={
            'class':'form-control'
        }
    ))
    
    class Meta:
        model = Receta
        fields = ('titulo', 'receta', 'autor', 'preparacion', 'imagen', 'fechingreso',)