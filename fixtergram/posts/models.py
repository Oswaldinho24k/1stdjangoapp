from django.db import models

class PostModel(models.Model):
	titulo = models.CharField(max_length=140)
	likes = models.IntegerField()
	descripcion = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField(upload_to='postimgs', blank=True, null=True)
	publicado = models.BooleanField(default=False)

	def __str__(self):
		return self.titulo

	#class Meta:
	#	ordering = 