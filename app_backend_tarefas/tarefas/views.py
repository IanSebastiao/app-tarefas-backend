from django.shortcuts import render

from rest_framework import generics
from .models import Tarefa
from .serializers import TarefaSerializer

class TarefaListCreateView(generics.ListCreateAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer
    
class TarefaRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarefa.objects.all()
    serializer_class = TarefaSerializer

# Create your views here.
