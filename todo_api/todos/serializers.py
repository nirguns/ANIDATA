from rest_framework import serializers
from .models import ToDo

class Todoserializer(serializers.ModelSerializer):
    class Meta:
        model= ToDo
        fields=('id','title','body')