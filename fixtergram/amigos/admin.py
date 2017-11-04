from django.contrib import admin
from .models import Amigo

# Register your models here.

class AdminAmigo(admin.ModelAdmin):
	prepopulated_fields = {"slug":("nombre","descripcion")}

admin.site.register(Amigo, AdminAmigo)


