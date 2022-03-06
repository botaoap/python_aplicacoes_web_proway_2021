from django.contrib import admin
from .models import TpPessoa, CPFCNPJ, UF, Cidade, Cliente

# Register your models here.
class VisualizaCLiente(admin.ModelAdmin):
    list_display = ['id', 'nome', 'cpfcnpj','estado_civil']
    list_display_links = ['id','nome']
    list_per_page = 5
    # search_fields = ['nome','email']
    # fields = ['nome', 'email', 'estadoCivil']
    fieldsets = (
        ('Básico', {'fields':('nome','cpfcnpj','genero','data_nasc','estadoCivil')}),
        ('Opicional',{'fields':('filho','carro')}),
        ('Financeiro',{'fields':('profissao','renda')})
    )
    
admin.site.register(TpPessoa)
admin.site.register(CPFCNPJ),
admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Cliente, VisualizaCLiente)