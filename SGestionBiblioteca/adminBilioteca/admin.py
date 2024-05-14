from django.contrib import admin
from adminBilioteca.models import Libro
from adminBilioteca.models import Usuario
from adminBilioteca.models import Prestamo
from adminBilioteca.models import Devolucion
from adminBilioteca.models import Genero
from adminBilioteca.models import Editorial



# Register your models here.
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Prestamo)
admin.site.register(Devolucion)
admin.site.register(Genero)
admin.site.register(Editorial)
