from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from posts import urls as postsUrls
from django.conf import settings
from django.views.static import serve
from amigos import urls as amigosurls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', TemplateView.as_view(template_name='home.html')),
    url(r'^posts/', include(postsUrls)),
    url(r'^amigos/', include(amigosurls)),

    url(
    	regex=r'^media/(?P<path>.*)$',
    	view=serve,
    	kwargs={'document_root':settings.MEDIA_ROOT}
    	),

]
