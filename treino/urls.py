from django.urls import path
from . import views

urlpatterns = [
    path('onboarding/', views.onboarding_view, name='onboarding'),
    path('treino/', views.mostrar_treino, name='mostrar_treino'),
]
