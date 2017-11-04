from django.conf.urls import url
from .views import PostListView, PostDetailView

urlpatterns = [
	url(r'^$', PostListView.as_view()),
	url(r'^detalle/(?P<id>[0-9]+)/$', PostDetailView.as_view()),
]