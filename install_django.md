# Django Install
- (Django)[https://www.djangoproject.com]

## How to install
- (Install)[https://docs.djangoproject.com/en/4.0/topics/install/]

## Começando o Projeto utilizando CMD:
- python -m pip install --upgrade pip 

## Atualizar pip
- pip install virtualenv
 
## Instala Criador de diretórios Virtuais
- cd / (Para voltar para pasta razi no c😊
- mkdir NomeDaPastaDoProjeto (Criar pasta onde projeto vai ficar)
- cd NomeDaPastaDoProjeto (Acessar pasta criada)
- python -m venv nomeDoSeuAmbienteVirtual

## (Criando ambiente Virtual)
- nomedoseuambientevirtual\Scripts\Activate.bat

## Instalando DJANGO (Ativar Ambiente)
- pip install Django

# COMANDOS DJANGO
- django-admin startproject NomeDoSite

## Cria Seu Primeiro Site
- cd NomeDoSite -> Acesar diretório do Site
- python manage.py migrate -> Iniciar nosso novoProjeto
- python manage.py createsuperuser -> criar usuário 
- python manage.py runserver 8080 🡪 coloca site no ar 
- CTR + C para projeto

## Criando um app para o site
- python manage.py startapp NomeDoApp

## Ativando Venv(linux)
- source bin/activate

## Desativando Venv(linux)
- deactivate

## Editando Arquivos do App para criar os Polls
- Admin.py
- from django.contrib import admin from polls.models import Question, 

## Choice
- admin.site.register(Question) admin.site.register(Choice)
- views.py
- from django.http import HttpResponse
- def index(request): return HttpResponse("Hello, world. You're at the polls index.")


## Criar na pasta do APP o urls.py
- from django.urls import path
- from . import views
- from django.urls.conf import include
`urlpatterns = [path('', views.index, name='index')]`

## Adicionar parâmetro de referencia no urls.py da bate do site
`path('meuApp/', include("meuApp.urls"))`