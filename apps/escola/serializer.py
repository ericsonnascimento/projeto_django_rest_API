from rest_framework import serializers
from escola.models import Aluno, Curso


#os dados de fields são os que serão exibidos no retorno do Json, podemos ocultar qualquer campo, podemos utilizar campo a campo ou simplesmente __all__.
class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'