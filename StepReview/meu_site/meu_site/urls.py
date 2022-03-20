"""meu_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from .views import cadastra_cidade, cadastra_servico, home, lista_cursos, cadastra_cliente, lista_tipos_pessoa, lista_ufs, lista_cidades
from .views import lista_clientes, lista_produtos, cadastra_produto, lista_servicos, cadastra_tipos_pessoa
from .views import cadastra_uf, altera_cidade, altera_produto, altera_cliente, altera_servico, altera_tipos_pessoa, altera_uf
from .views import exclui_cidade, exclui_cliente, exclui_produto, exclui_servico, exclui_tipos_pessoa, exclui_uf
from .views import lista_categorias, altera_categoria, exclui_categoria, cadastra_categoria
from .views import lista_EstadoCivil, alterar_EstadoCivil, cadastra_EstadoCivil, excluir_EstadoCivil

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home',home),
    path('lista-categoria',lista_categorias),
    path('cadastro-categoria',cadastra_categoria),
    path('altera-categoria/<int:id>',altera_categoria),
    path('exclui-categoria/<int:id>',exclui_categoria),
    path('lista-produto',lista_produtos),
    path('cadastro-produto',cadastra_produto),
    path('altera-produto/<int:id>',altera_produto),
    path('exclui-produto/<int:id>',exclui_produto),
    path('lista-cliente',lista_clientes),
    path('cadastro-cliente',cadastra_cliente),
    path('altera-cliente/<int:id>',altera_cliente),
    path('exclui-cliente/<int:id>',exclui_cliente),
    path('lista-servico',lista_servicos),
    path('cadastro-servico',cadastra_servico),
    path('altera-servico/<int:id>',altera_servico),
    path('exclui-servico/<int:id>',exclui_servico),
    path('lista-tp-pessoa',lista_tipos_pessoa),
    path('cadastro-tp-pessoa',cadastra_tipos_pessoa),
    path('altera-tp-pessoa/<int:id>',altera_tipos_pessoa),
    path('exclui-tp-pessoa/<int:id>',exclui_tipos_pessoa),
    path('lista-uf',lista_ufs),
    path('cadastro-uf',cadastra_uf),
    path('altera-uf/<int:id>',altera_uf),
    path('exclui-uf/<int:id>',exclui_uf),
    path('lista-cidade',lista_cidades),
    path('cadastro-cidade',cadastra_cidade),
    path('altera-cidade/<int:id>',altera_cidade),
    path('exclui-cidade/<int:id>',exclui_cidade),
    path('lista-estado-civil',lista_EstadoCivil),
    path('cadastro-estado-civil',cadastra_EstadoCivil),
    path('altera-estado-civil/<int:id>',alterar_EstadoCivil),
    path('exclui-estado-civil/<int:id>',excluir_EstadoCivil),
    path('contato',TemplateView.as_view(template_name='contato.html')),
    path('acesso',TemplateView.as_view(template_name='login.html')), 
    path('cursos',lista_cursos),
    path('',home),
]
