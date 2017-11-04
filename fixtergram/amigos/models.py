from django.db import models

# Create your models here.
class Amigo(models.Model):
	LUGARES = (
			('escuela', 'escuela'),
			('parque', 'parque'),
			('fiesta', 'fiesta')
			)
	nombre = models.CharField(max_length=100)
	followers = models.IntegerField()
	descripcion = models.TextField()
	foto = models.ImageField(upload_to='amigos_fotos')
	slug = models.SlugField(unique=True)
	cumpleanos = models.DateTimeField(auto_now_add=False, db_index=True)
	lugar_donde_nos_conocimos = models.CharField(choices=LUGARES, max_length=200, blank=True, null=True)

	def __str__(self):
		return 'mi amigo el {}'.format(self.nombre)

