from django.conf.urls import include, url
from django.contrib import admin, auth
from django.conf.urls.static import static
from django.conf import settings
from main import views as main_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^', include('django.contrib.auth.urls')),
    url(r'^accounts/login/$', auth.views.login, {'template_name': 'admin/login.html'}),
    url(r'^accounts/logout/$', auth.views.logout, {'template_name': 'admin/logout.html'}),
    url(r'^$', main_views.camlist, name='camlist'),
    url(r'^test$', main_views.test, name='test'),
    url(r'^socket_cam_(?P<pk>\d+)$', main_views.image_response, name='image_response'),
    url(r'^connect_cam_(?P<pk>\d+)', main_views.connect_video_stream, name='connect_video_stream'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
