## Criando Ambiente Virtiual Passo a Passo
### CMD Setp1
1. ` mkdir <nome-pasta> ` Criar uma pasta
2. ` cd <nome-pasta> ` Entrar na pasta
3. ` pip install virtualenv ` Instalacao do Virtual Venv
4. ` python3 -m venv <nome-ambiente-virtual> ` Criando Ambiente Virtual
5. ` cd <nome-ambiente-virtual> ` Entrar na pasta do Ambiente Virtual
6. ` source bin/activate ` Ativar Ambiente Virtual
7. ` deactivate ` Destivar Ambiente Virtual

### Achar caminho de pastas Terminal
- pwd
### CMD Setp2
1. `python3 manage.py` Verificar quais comandos estao disponiveis
2. `python3 manage.py startapp produto` Criar um App
3. `python3 manage.py makemigration` Inserir o App na Core
4. `python3 manage.py migrate` Validar Insercao do App na Core
5. 