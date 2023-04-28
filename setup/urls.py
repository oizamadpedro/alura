from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers, permissions
from django.conf import settings
from django.conf.urls.static import static
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls.static import static
from escola.views import index


schema_view = get_schema_view(
    openapi.Info(
        title="escola",
        default_version='v1',
        description="Escola e Aluno",
        terms_of_service="#",
        contact=openapi.Contact(email="c3po1@alura.com.br"),
        license=openapi.License(name="pedro"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)


router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='Alunos')
router.register('cursos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('controle-geral/', admin.site.urls),
    path('', include(router.urls)),
    path('alunos/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('cursos/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
    name='schema_swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
    name='schema-redoc'),
    path('index.html', index, name='index'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
