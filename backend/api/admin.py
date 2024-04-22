from django.contrib import admin
from .models import ToDo

# Register your models here.
@admin.register(ToDo)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_done', 'user']
    search_fields = ['title']
    list_filter = ['is_done', 'user']