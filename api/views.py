from django.http import Http404, JsonResponse
from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *
from .pagination import *


class VagasList(APIView):
    def get(self, request):
        try:
            lista_vagas = Vaga.objects.all()
            paginator = PaginacaoVagas()
            result_page = paginator.paginate_queryset(lista_vagas, request)
            serializer = VagaSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        except Exception:
            return JsonResponse({'message': "Server Error."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        try:
            serializer = VagaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return JsonResponse({'message': "Server Error."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class VagaDetalhes(APIView):
    def get(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'message': "ID must be greater than zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga)
            return Response(serializer.data)
        except Vaga.DoesNotExist:
            return JsonResponse({'message': "Vaga not exist."},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'message': "Server Error."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def put(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'message': "ID must be greater than zero."},
                                     status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga, data-request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Vaga.DoesNotExist:
            return JsonResponse({'message': "Vaga not exist."},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'message': "Server Error."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'message': "ID must be greater than zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            vaga.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vaga.DoesNotExist:
            return JsonResponse({'message': "Vaga not exist."},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'message': "Server Error."},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
