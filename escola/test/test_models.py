from django.test import TestCase
from escola.models import Aluno

class AlunoModelTestCase(TestCase):
#TESTE DE UNIDADE

    def setUp(self):
        self.aluno = Aluno(
            nome='Pedro Augusto',
            #CPF = 'SEU CPF AQUI'
        )

    def test_verifica_atributos_do_aluno(self):
        """Verifica atributos do aluno"""
        self.assertEqual(self.aluno.nome, 'Pedro Augusto')
        self.assertEqual(self.aluno.cpf, 'seu cpf')