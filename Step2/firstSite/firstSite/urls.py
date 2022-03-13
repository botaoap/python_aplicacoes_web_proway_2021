"""firstSite URL Configuration

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
from .views import home, lista_cidade, lista_tp_pessoa, lista_uf, lista_cliente, lista_produto, lista_servico, lista_categoria
from .views import cadastro_cliente, cadastro_produto, cadastro_cidade, cadastro_servico, cadastro_tp_pessoa, cadastro_uf, cadastro_categoria
from .views import altera_cidade, altera_cliente, altera_produto, altera_servico, altera_tp_pessoa, altera_uf, altera_categoria
from .views import exclui_cidade, exclui_cliente, exclui_produto, exclui_servico, exclui_tp_pessoa, exclui_uf, exclui_categoria

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home', home),
    path('contato', TemplateView.as_view(template_name='contato.html')),
    path('login', TemplateView.as_view(template_name='login.html')),
    path('lista-produto', lista_produto),
    path('lista-cliente', lista_cliente),
    path('lista-servico', lista_servico),
    path('lista-tp-pessoa', lista_tp_pessoa),
    path('lista-uf', lista_uf),
    path('lista-cidade', lista_cidade),
    path('lista-categoria', lista_categoria),
    path('cadastro-produto', cadastro_produto),
    path('cadastro-cliente',cadastro_cliente),
    path('cadastro-servico',cadastro_servico),
    path('cadastro-tp-pessoa',cadastro_tp_pessoa),
    path('cadastro-uf',cadastro_uf),
    path('cadastro-cidade',cadastro_cidade),
    path('cadastro-categoria',cadastro_categoria),
    path('altera-produto/<int:id>', altera_produto),
    path('altera-cliente', altera_cliente),
    path('altera-servico/<int:id>', altera_servico),
    path('altera-tp-pessoa/<int:id>', altera_tp_pessoa),
    path('altera-uf/<int:id>', altera_uf),
    path('altera-cidade/<int:id>', altera_cidade),
    path('altera-categoria/<int:id>', altera_categoria),
    path('exclui-produto/<int:id>', exclui_produto),
    path('exclui-cliente/<int:id>', exclui_cliente),
    path('exclui-servico/<int:id>', exclui_servico),
    path('exclui-tp-pessoa/<int:id>', exclui_tp_pessoa),
    path('exclui-uf/<int:id>', exclui_uf),
    path('exclui-cidade/<int:id>', exclui_cidade),
    path('exclui-categoria/<int:id>', exclui_categoria),
    path('', home),
]