from django.contrib import admin

#importando os nosso modelos (quem conversa com o DB)
from apps.escola.models import Aluno, Curso

class Alunos(admin.ModelAdmin):
        list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
        list_display_links = ('id', 'nome')
        search_fields = ('nome',)
        list_per_page = 20

#obrigados a passar dois argumentos; 1° a classe models(Aluno), 2° a classe admin(Aluno)
admin.site.register(Aluno, Alunos)

class Cursos(admin.ModelAdmin):
    list_display = ('id', 'codigo_curso', 'descricao')
    list_display_links = ('id', 'codigo_curso')
    search_fields = ('codigo_curso',)

#obrigados a passar dois argumentos; 1° a classe models(Curso), 2° a classe admin(Cursos)
admin.site.register(Curso, Cursos)
