from rest_framework import serializers
from .models import *


class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga
        fields = ['id','titulo','descricao','salario','tipo_contrato','status']
