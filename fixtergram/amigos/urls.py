from django.conf.urls import url
from .views import AmigosListView, AmigosDetailView

urlpatterns = [
	url(r'^$', AmigosListView.as_view()),
	url(r'^(?P<slug>[\w-]+)$', AmigosDetailView.as_view()),
]