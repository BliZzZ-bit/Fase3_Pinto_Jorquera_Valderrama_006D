from django.urls import path
from . import views
urlpatterns = [
    
    path('',views.index,name='index'),
    path('novedades/',views.novedades,name='novedades'),
    path('dulces/',views.dulces,name='dulces'),
    path('saladas/',views.saladas,name='saladas'),
    path('pret/',views.pret,name='pret'),
    path('pie/',views.pie,name='pie'),
    path('capu/',views.capu,name='capu'),
    path('bebidas/',views.bebidas,name='bebidas'),
    path('autores/', views.AutorListView.as_view(), name='autores'),
    path('recetas/', views.RecetaListView.as_view(), name='recetas'),
    path('autor/<int:pk>', views.AutorDetailView.as_view(), name='autor-detail'),
    path('receta/<int:pk>', views.RecetaDetailView.as_view(), name='receta-detail'),
]

urlpatterns += [
    path('autor/create/',views.AutorCreate.as_view(), name='autor_create'),
    path('autor/<int:pk>/update/',views.AutorUpdate.as_view(), name='autor_update'),
    path('autor/<int:pk>/delete/',views.AutorDelete.as_view(), name='autor_delete'),
    path('receta/create/',views.RecetaCreate.as_view(), name='receta_create'),
    path('receta/<int:pk>/update/',views.RecetaUpdate.as_view(), name='receta_update'),
    path('receta/<int:pk>/delete/',views.RecetaDelete.as_view(), name='receta_delete'),

]