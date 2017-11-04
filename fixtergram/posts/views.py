from django.shortcuts import render
from django.views.generic import View
from .models import PostModel

# Create your views here.

class PostListView(View):
	def get(self, request):
		template_name = 'posts.html'
		postitos = PostModel.objects.all()
		context = {'posts':postitos}
		return render(request, template_name, context)

class PostDetailView(View):
	def get(self, request, id):
		template_name = 'postDetail.html'
		print("Hola")
		post = PostModel.objects.get(id=id)
		context = {'post':post}
		return render(request, template_name, context)

