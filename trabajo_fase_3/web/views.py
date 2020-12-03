from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Preparacion, Receta, Autor

# Create your views here.
def index(request):

    num_recetas=Receta.objects.all().count()
    num_autores=Autor.objects.count()

    return render(
        request,
        'index.html',
        context={'num_recetas':num_recetas, 'num_autores':num_autores},
    )

def novedades(request):
    return render(
        request, 
        'novedades.html',
)

def dulces(request):
    return render(
        request, 
        'dulces.html',
)

def saladas(request):
    return render(
        request, 
        'saladas.html',
)

def bebidas(request):
    return render(
        request, 
        'bebidas.html',
)

def pret(request):
    return render(
        request, 
        'pret.html',
)

def pie(request):
    return render(
        request, 
        'pie.html',
)

def capu(request):
    return render(
        request, 
        'capu.html',
)

class AutorCreate(CreateView):
    model = Autor
    fields = ['pnombre', 'papellido', 'fechanac', 'fechamuerte']

class AutorUpdate(UpdateView):
    model = Autor
    fields = ['pnombre', 'papellido', 'fechanac', 'fechamuerte']

class AutorDelete(DeleteView):
    model = Autor
    success_url = reverse_lazy('index')

class RecetaCreate(CreateView):
    model = Receta
    fields = ['titulo', 'receta', 'fechingreso', 'autor','imagen', 'preparacion']

class RecetaUpdate(UpdateView):
    model = Receta
    fields = ['titulo', 'receta', 'fechingreso', 'autor','imagen', 'preparacion']

class RecetaDelete(DeleteView):
    model = Receta
    success_url = reverse_lazy('index')    

from django.views import generic

class AutorListView(generic.ListView):
    model = Autor
    template_name = 'templates/web/autor_list.html'
    queryset = Autor.objects.all()

    paginate_by = 10

class RecetaListView(generic.ListView):
    model = Receta
    template_name = 'templates/web/receta_list.html'
    queryset = Receta.objects.all()
    paginate_by = 5    


class AutorDetailView(generic.DetailView):
    model = Autor

class RecetaDetailView(generic.DetailView):
    model = Receta
    