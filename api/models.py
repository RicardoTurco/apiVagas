from django.db import models


TIPO_CONTRATO_CHOICES = (
    ('PJ', 'Pessoa Jurídica'),
    ('CLT', 'Consolidação das leis do Trabalho')
)

class Vaga(models.Model):
    titulo = models.CharField(max_length=30, null=False)
    descricao = models.TextField(null=False)
    salario = models.FloatField(null=False)
    tipo_contrato = models.CharField(choices=TIPO_CONTRATO_CHOICES, null=False, max_length=50)
    status = models.BooleanField(null=False, default=1)

    def __str__(self):
        return self.titulo
