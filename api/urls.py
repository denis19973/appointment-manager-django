from django.conf.urls import url, include
from api.views import get_appointment_data

urlpatterns = [
    url(r'^appointments/$', get_appointment_data, name='appointments-data'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
