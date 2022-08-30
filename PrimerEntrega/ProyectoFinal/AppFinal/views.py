from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppFinal.models import Author, Source, Article
from AppFinal.forms import AuthorFormulario, SourceFormulario, ArticleFormulario


# Create your views here.
def inicio(request):

      return render(request, "inicio.html")


def author(request):     
      if request.method == 'POST':

            miFormulario = AuthorFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  author = Author (nombre=informacion['nombre'], DNI=informacion['DNI'],
                   email=informacion['email'], telefono=informacion['telefono']) 

                  author.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= AuthorFormulario() #Formulario vacio para construir el html

      return render(request, "author.html", {"miFormulario":miFormulario})

def sources(request):

      if request.method == 'POST':

            miFormulario = SourceFormulario(request.POST) #aquí mellega toda la información del html

            print(miFormulario)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data

                  source = Source (nombre=informacion['nombre']) 

                  source.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= SourceFormulario() #Formulario vacio para construir el html

      return render(request, "source.html", {"miFormulario":miFormulario})


  

def buscar(request):

      if  request.GET["nombre"]:

	      #respuesta = f"Estoy buscando la camada nro: {request.GET['nombre'] }" 
            autor = request.GET['nombre'] 
            autores = Author.objects.filter(nombre__icontains=autor)

            return render(request, "inicio.html", {"autores":autores, "autor":autor })

      else: 

	      respuesta = "No enviaste datos"

      #No olvidar from django.http import HttpResponse
      return HttpResponse(respuesta)

def article(request):     
      if request.method == 'POST':

            miFormulario = ArticleFormulario(request.POST) #aquí mellega toda la información del html
           # if Author.objects.filter(DNI__icontains=miFormulario.DNIAutor):
            #      autor = Author.objects.filter(DNI__icontains=miFormulario.DNIAutor)
            #else:
            #      miFormulario.DNIAutor="false"

            #if Source.objects.filter(nombre__icontains=miFormulario.fuente):
            #      fuente= Source.objects.filter(nombre__icontains=miFormulario.fuente)
            #else:
            #      miFormulario.fuente=0
            
            print(miFormulario)
            #print(autor)
            #print(fuente)

            if miFormulario.is_valid:   #Si pasó la validación de Django

                  informacion = miFormulario.cleaned_data
                  autor = Author.objects.filter(DNI__icontains='DNIAutor')
                  fuente= Source.objects.filter(nombre__icontains='fuente')
                  article = Article (nombre=informacion['nombre_articulo'], descripcion=informacion['descripcion'])
                  #article.Author=autor
                  article.source=fuente 

                  article.save()

                  return render(request, "inicio.html") #Vuelvo al inicio o a donde quieran

      else: 

            miFormulario= ArticleFormulario() #Formulario vacio para construir el html

      return render(request, "author.html", {"miFormulario":miFormulario})
