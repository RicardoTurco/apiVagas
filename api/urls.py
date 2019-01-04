from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = [
    url(r'vagas$', VagasList.as_view()),
    url(r'vagas/(?P<pk>[0-9]+)$', VagaDetalhes.as_view()),
]
