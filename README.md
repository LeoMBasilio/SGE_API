
Esse material tem como base o projeto da última aula presente no link: ```https://github.com/LeoMBasilio/SGE_API.git```

## Estrutura Geral do Projeto

A estrutura apresentada refere-se a um projeto Django dividido em dois aplicativos principais:

1. **school**: Uma aplicação que provavelmente lida com a lógica de negócio relacionada a uma escola.
2. **setup**: Contém a configuração global do projeto Django.

Junto a isso, há arquivos auxiliares e uma pasta chamada `venv`, que representa o ambiente virtual do projeto.

### Pasta `school`

#### 1. `__pycache__`

Esta pasta é gerada automaticamente pelo Python e armazena os arquivos compilados (.pyc). Eles ajudam a acelerar a execução do código, mas podem ser ignorados no desenvolvimento.

#### 2. `migrations`

Esta subpasta é usada para rastrear alterações no modelo de dados do Django. Contém arquivos de migração gerados automaticamente pelo comando:

```bash
python manage.py makemigrations
```

Esses arquivos ajudam a sincronizar o banco de dados com os modelos definidos em `models.py`.

- **Exemplo:**
  Um arquivo de migração pode conter algo como:

```python
class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
```

#### 3. `admin.py`

Contém a configuração para registrar modelos no painel administrativo do Django.

- **Exemplo:**

```python
from django.contrib import admin
from .models import Student

admin.site.register(Student)
```

Isso torna o modelo `Student` visível e gerenciável no admin.

#### 4. `apps.py`

Define configurações específicas para a aplicação. O Django usa este arquivo para identificar a aplicação.

- **Exemplo:**

```python
from django.apps import AppConfig

class SchoolConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school'
```

#### 5. `models.py`

Define os modelos (estruturas de dados) usados pela aplicação, que são traduzidos para tabelas no banco de dados.

- **Exemplo:**

```python
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
```

#### 6. `serializers.py`

Usado para converter dados entre tipos complexos (como objetos de modelo) e formatos como JSON ou XML, geralmente usado em APIs Django Rest Framework.

- **Exemplo:**

```python
from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
```

#### 7. `tests.py`

Usado para criar testes automatizados para verificar o funcionamento da aplicação.

- **Exemplo:**

```python
from django.test import TestCase
from .models import Student

class StudentTestCase(TestCase):
    def setUp(self):
        Student.objects.create(name="John", age=15)

    def test_student_age(self):
        student = Student.objects.get(name="John")
        self.assertEqual(student.age, 15)
```

#### 8. `views.py`

Define a lógica para manipular requisições e retornar respostas.

- **Exemplo:**

```python
from django.http import JsonResponse
from .models import Student


def student_list(request):
    students = Student.objects.all()
    data = {"students": list(students.values())}
    return JsonResponse(data)
```

### Pasta `setup`

#### 1. `__pycache__`

Semelhante ao descrito na pasta `school`.

#### 2. `__init__.py`

Indica que esta pasta é um módulo Python. Geralmente, permanece vazio.

#### 3. `asgi.py`

Configuração para ASGI (Asynchronous Server Gateway Interface), usada para suportar aplicações assíncronas no Django.

#### 4. `settings.py`

Contém as configurações gerais do projeto, como definições de banco de dados, instalação de apps e configurações de segurança.

- **Exemplo:** Adicionar uma aplicação na lista de apps instalados:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    ...
    'school',
]
```

#### 5. `urls.py`

Define as URLs do projeto e suas respectivas views.

- **Exemplo:**

```python
from django.contrib import admin
from django.urls import path
from school import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', views.student_list, name='student-list'),
]
```

#### 6. `wsgi.py`

Configuração para WSGI (Web Server Gateway Interface), usada para implantação em servidores.

### Outros Arquivos e Pastas

#### 1. `.gitignore`

Lista arquivos e pastas que devem ser ignorados pelo controle de versão Git. Exemplo comum:

```
venv/
__pycache__/
db.sqlite3
```

#### 2. `db.sqlite3`

Banco de dados padrão do Django, usado para desenvolvimento.

#### 3. `manage.py`

Script principal para interagir com o projeto. Exemplos de comandos:

```bash
python manage.py runserver  # Inicia o servidor
python manage.py makemigrations  # Cria migrações
python manage.py migrate  # Aplica migrações
```

#### 4. `README.md`

Documento que geralmente explica o objetivo e as instruções do projeto.

### Ambiente Virtual (`venv`)

Contém as dependências do projeto isoladas do sistema principal. Ative-o com:

```bash
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
```
