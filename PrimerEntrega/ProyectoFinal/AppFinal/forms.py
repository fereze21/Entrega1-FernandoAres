from django import forms

class AuthorFormulario(forms.Form):   
    nombre= forms.CharField(max_length=30)
    email= forms.EmailField()
    DNI= forms.IntegerField()
    telefono=forms.IntegerField()

class SourceFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)

class ArticleFormulario(forms.Form):
    nombre_articulo = forms.CharField(max_length=30)
    descripcion = forms.CharField(max_length=30)
    DNIAutor= forms.IntegerField()
    fuente=forms.CharField(max_length=30)
    
    