from django.contrib import admin
from .models import TpPessoa, CPFCNPJ, UF, Cidade, Cliente

# Register your models here.
admin.site.register(TpPessoa)
admin.site.register(CPFCNPJ),
admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Cliente)