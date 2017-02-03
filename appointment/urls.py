from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.contrib.auth.views import logout
from email_authentication import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/', views.login_view, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^swingtime/', include('swingtime.urls')),
]
