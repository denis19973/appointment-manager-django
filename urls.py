from django.contrib import admin
from django.conf.urls import include, url
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    url(r'^api/', include('api.urls')),
    url(r'^appointment/', include('appointment.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
]
