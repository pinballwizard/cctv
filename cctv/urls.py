from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from main import views as main_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'template_name': 'admin/logout.html'}),
    url(r'^$', main_views.camlist, name='camlist'),
    url(r'^test', main_views.test, name='test'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
