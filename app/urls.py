from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('treino.urls')),  # substitua 'treino' pelo nome do seu app
]
