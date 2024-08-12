# Define quien consulta
from .models import Project
from rest_framework import viewsets, permissions
from . serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Consultar todos los datos de una tabla
    permission_classes = [permissions.AllowAny] # Permisos
    serializer_class = ProjectSerializer