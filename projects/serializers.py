from rest_framework import serializers
from .models import project


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = project
        fields = ('id', 'titulo', 'descripcion')
        read_only_fields =('created_at', )


def validacion(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("El título es muy corto corto.")
        return value

def validacionNeg(self, value):
     if value < 0:
          raise serializers.ValidationError(" No puede ser negativo el stock")
     return value