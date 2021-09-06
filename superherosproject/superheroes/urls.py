from django.urls import path
from . import views


app_name = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('detail/<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create'),
    path('<int:superhero_id>/delete/', views.delete, name='delete')
]