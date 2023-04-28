from django.test import TestCase
from escola.models import Aluno
from escola.serializer import AlunoSerializer

class AlunoSerializerTestCase(TestCase):

    def setUp(self):
        self.aluno = Aluno(
            nome='Pedro Augusto',
            #cpf='SEU CPF AQUI'
            email='oizamadpedro@gmail.com'
        )
        self.serializer = AlunoSerializer(instance=self.aluno)
    
    def test_verifica_campos_serializados(self):
        """Teste que verifica os campos que estão sendo serializados"""
        data = self.serializer.data
        self.assertEqual(set(data.keys()), set(['nome', 'cpf', 'email', 'id', 'rg', 'celular', 'foto']))

    def test_verifica_conteudo_dos_campos_serializados(self):
        """Teste que verifica conteudo dos campos serializados"""
        data = self.serializer.data
        self.assertEqual(data['nome'], self.aluno.nome)
        self.assertEqual(data['rg'], self.aluno.rg)