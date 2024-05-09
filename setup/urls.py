from django.contrib import admin
from django.urls import path
from documents.views import documentos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('documentos/', documentos)
]
