from cgitb import reset
from seminarioApi.models import seminario
from django.shortcuts import render, redirect
from seminarioApi.forms import FormReserva
from django.shortcuts import render
from .serializers import seminarioSerializer
from .models import seminario
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import Http404
# Create your views here.


def index(request):
    return render(request, 'index.html')

def listadoReservas(request):
    reservas = seminario.objects.all()
    data = {'reservas': reservas}
    return render(request, 'reservas.html', data)

def agregarReserva(request):
    form = FormReserva()
    if request.method == 'POST':
        form = FormReserva(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarReserva.html', data)

def eliminarReserva(request, id):
    res = seminario.objects.get(id = id)
    res.delete()
    return redirect('/reservas')

def actualizarReserva(request, id):
    res = seminario.objects.get(id = id)
    form = FormReserva(instance=res)
    if request.method == 'POST' :
        form = FormReserva(request.POST, instance=res)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarReserva.html', data)

class ListaParticipantes(APIView):
    def get(self, request):
        semi = seminario.objects.all()
        serial = seminarioSerializer(semi, many=True)
        return Response(serial.data)

    def post(self, request):
        serial = seminarioSerializer(data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=status.HTTP_201_CREATED)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)


class DetalleParticipantes(APIView):
    def get_object(self, pk):
        try:
            return seminario.objects.get(id=pk)
        except seminario.DoesNotExist:
            return Http404

    def get(self, request, pk):
        semi = self.get_object(pk)
        serial = seminarioSerializer(semi)
        return Response(serial.data)

    def put(self, request, pk):
        semi = self.get_object(pk)
        serial = seminarioSerializer(semi, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        return Response(serial.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        semi = self.get_object(pk)
        semi.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
