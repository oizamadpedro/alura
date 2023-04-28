from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from django.contrib.auth import authenticate
from rest_framework import status
from django.urls import reverse

class AuthenticationTestCase(APITestCase):

    def setUp(self):
        self.list_url = reverse('Alunos-list')
        self.user = User.objects.create_user('c3pao1', password='123456')

    def test_autenticacao_user_com_credenciais_corretas(self):
        """Teste que verifica a autenticacao de um user com credenciais corretas"""
        user = authenticate(username='c3pao1', password='123456')
        self.assertTrue((user is not None) and user.is_authenticated)
    
    #def test_requisicao_get_nao_autorizada(self):
    #    """Teste que verifica uma requisição GET sem autenticar"""
    #    response = self.client.get(self.list_url)
    #   self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_autenticacao_de_user_com_username_incorreto(self):
        user = authenticate(username='c3pao', password='123456')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_autenticacao_de_user_com_password_incorreto(self):
        user = authenticate(username='c3pao1', password='1234564')
        self.assertFalse((user is not None) and user.is_authenticated)

    def test_requisicao_get_nao_autorizada(self):
        """Teste que verifica uma requisição GET de um user autenticado"""
        self.client.force_authenticate(self.user)
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)