from django.contrib import admin
from documents.models import Document

# Register your models here.
class Documents(admin.ModelAdmin):
    list_display = ('id', 'name', 'register', 'rg', 'cpf', 'doc_type', 'birthday')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'register', 'cpf', 'rg')
    list_filter = ('doc_type',)
    list_per_page = 20
    ordering = ('name',)

admin.site.register(Document, Documents)