from django.db import models

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    genero = models.CharField(max_length=50)
    año_publicacion = models.IntegerField()
    numero_ejemplares = models.IntegerField()

    def _str_(self):
        return self.titulo
    
from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20)
    correo_electronico = models.EmailField()

    def _str_(self):
        return self.nombre
    
from django.db import models

class Prestamo(models.Model):
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha_prestamo = models.DateField()
    fecha_vencimiento = models.DateField()

    def _str_(self):
        return f"Prestamo de {self.libro.titulo} a {self.usuario.nombre}"
    
from django.db import models

class Devolucion(models.Model):
    prestamo = models.OneToOneField(Prestamo, on_delete=models.CASCADE)
    fecha_devolucion = models.DateField()

    def _str_(self):
        return f"Devolucion de {self.prestamo.libro.titulo} de {self.prestamo.usuario.nombre}"

from django.db import models

class Genero(models.Model):
    nombre = models.CharField(max_length=50)

    def _str_(self):
        return self.nombre

from django.db import models

class Editorial(models.Model):
    nombre = models.CharField(max_length=100)

    def _str_(self):
        return self.nombre