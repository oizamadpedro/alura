from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula
from escola.validators import *

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf':"CPF INVALIDO!"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Não inclua numeros neste campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError({'celular': "O Número de celular deve seguir este modelo: 11 91234-1234"})
        return data

class AlunoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'email']

class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []

class CursoSerializer(serializers.ModelSerializer):
    exibe = AlunoSerializer2()
    class Meta:
        model = Curso
        fields = '__all__'
    

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']


class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'celular', 'email']
