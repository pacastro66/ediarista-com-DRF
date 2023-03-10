# Projeto e-diaristas

### Instalando o projeto

### Para remover o link do projeto 
`git remote remove origin`

## para criar novo link com o projeto
`git remote add origin https://github.com/pacastro66/ediarista-com-DRF  **exemplo**`
##para renomear o projeto
`git branch -M main`
`git push -u origin main`



### Clonar o projeto dentro de uma pasta
`git clone https://github.com/pacastro66/ediaristas1`

### criar a virtual env
`python -m venv venv`

### ativar a virtual env
`Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
`venv\Scripts\activate`

### instalar dependencias
`pip install -r requirements.txt`

### Alterar configurações do BD no arquivo `settings.py`
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco_de_dados',
        'HOST': 'host_do_bd',
        'PORT': 'porta_bd',
        'USER':'usuario_bd',
        'PASSWORD':'senha_bd'

    }
}
``` 

### Migrar banco de dados
`python manage.py migrate`
### Iniciar o servidor
`py manage.py runserver`