from rest_framework import generics
from .models import ToDo
from .serializers import Todoserializer


class ListToDo( generics.ListAPIView):
    queryset=ToDo.objects.all()
    serializer_class = Todoserializer




class DetaliToDo(generics.RetrieveAPIView):
    queryset=ToDo.objects.all()
    serializer_class = Todoserializer

    







# Create your views here.
