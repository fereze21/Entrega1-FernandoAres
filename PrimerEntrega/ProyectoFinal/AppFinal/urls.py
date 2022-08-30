from django.urls import path

from AppFinal import views


urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('author', views.author, name="Author"),
    path('source', views.sources, name="Source"),
    path('article', views.article, name="Article"),
    #path('cursoFormulario', views.cursoFormulario, name="CursoFormulario"),
    #path('profesorFormulario', views.profesorFormulario, name="ProfesorFormulario"),
    #path('busquedaCamada',  views.busquedaCamada, name="BusquedaCamada"),
    path('buscar/', views.buscar),
   
]

