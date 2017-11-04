from django.shortcuts import render
from .models import Amigo
from django.views.generic import View

# Create your views here.a

class AmigosListView(View):
	def get(self, request):
		template_name = 'amigos.html'
		amigos = Amigo.objects.all()
		context = {
			'amigos':amigos
		}
		return render(request, template_name, context)

class AmigosDetailView(View):
	def get(self, request, slug):
		
		template_name = 'amigos_detail.html'
		amigo = Amigo.objects.get(slug=slug)
		context = {
			'amigo':amigo
		}
		return render(request, template_name, context)

