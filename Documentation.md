## Описание реализаций в приложении
- models
``` 
Описание моделей для создания их в Дата Базе
verbose_name: Удобочитаемое имя для поля
max_length: Ограничение по количеству символов
CharField: Строковое поле, для строк малого и большого размера.
TextField: Для больших объемов текста
DateTimeField: Дата и время
ManyToManyField: Отношение многие ко многим
BooleanField: Поле истина/ложь.
- Tag
name = models.CharField(max_length=100, verbose_name='Имя Тега')
- Task
title = models.CharField(max_length=100, verbose_name='Заголовок')
description = models.TextField(max_length=500, verbose_name='Описание')
due_date = models.DateTimeField(null=True, blank=True, verbose_name='Срок выполнения')
tags = models.ManyToManyField(Tag, related_name='tasks', blank=True, verbose_name='Теги')
is_completed = models.BooleanField(default=False, verbose_name='Выполнение')
created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
```
- schema
``` 
Использвуется для расширенного описания каждого метода API - Документации API (drf_spectacular)
summary - краткое описание метода 
description - описание метода
responses - заменяет типовые описания статус кодов (200, 404 и т.п)
```
- serializers
``` 
1. Сериализация данных: При получении запроса на создание или обновление объекта Tag/Task,   
сериализатор проверяет входящие данные и преобразует их в формат, подходящий для сохранения   
в базе данных.
   
2. Десериализация данных: При чтении данных из базы данных (например, при запросе    
списка объектов Tag/Task), сериализатор преобразует данные из формата базы данных в JSON или    
другой формат, удобный для передачи клиенту.

fields = '__all__' - Указывает, что все поля модели Tag/Task должны быть включены в сериализацию.
```
- tests
``` 
Предусмотрено 2 тестирования. 
Создание Тегов. Проверка успешной передачи и изъятие на проверку из базы.
Создание Тега и задачи. Проверка успешной передачи и проверка успешной записи  
по Заголовку. 
```
- views
``` 
Содержит параметры Пагинации(постраничные данные)
- page_size = 10: Cтандартный размер страницы (количество объектов на одной странице).
- page_size_query_param = 'page_size': Позволяет изменять размер страницы через   
GET-параметр page_size в URL.
- max_page_size = 100: Ограничивает максимальный допустимый размер страницы.

TaskViewSet представляет собой ViewSet для работы с задачами (Task).
- http_method_names = ['get', 'post', 'patch', 'delete']: Определяет разрешённые методы    
для данного ViewSet. Следовать, Отправить, Изменить и Удалить.
- queryset = Task.objects.all().order_by('-created_at'): Определяет исходный набор данных   
(все задачи) и сортирует их по полю created_at в обратном порядке (по убыванию).
- serializer_class = TaskSerializer: Указывает, какой сериализатор использовать для    
преобразования данных задач в формат, пригодный для отправки клиенту.
- pagination_class = CustomPagination: Применяет настроенную ранее стратегию пагинации.

TagViewSet включает в себя разрешённые методы, сериализацию, пагинацию и сортировку.
- queryset = Tag.objects.all().order_by('name'): Все теги сортируются по полю name.
```
- urls
``` 
- DefaultRouter(): Создается экземпляр роутера, который автоматически генерирует  
стандартные маршруты для RESTful API, включая CRUD операции (create, read, update, delete).
- register(r'task', TaskViewSet, basename='tasks'): Регистрируется путь /task/ для    
доступа к Task через TaskViewSet. Параметр basename - для генерации именованных маршрутов.
- register(r'tags', TagViewSet, basename='tags'): Регистрация пути /tags/ для Tag через TagViewSet.

- path('admin/', admin.site.urls): Маршрут к административной панели Django.   
- path('', include(router.urls)): Включает все маршруты, созданные роутером.
- path('schema/', SpectacularAPIView.as_view(), name='schema'): Маршрут для генерации схемы    
OpenAPI для API.
- path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='docs'): Путь отображения  
интерактивной документации Swagger.
```
- admin
``` 
Регистрируем две модели (Task и Tag) в административной панели и определяем,   
какие поля будут отображаться в списке записей для каждой из моделей.
Task - ['title', 'description', 'due_date', 'is_completed', 'created_at']
Task - [Заголовок, Описание, Срок выполнения, Выполнение, Дата создания]
Tag - ['name']
Tag - [Теги]
```

## Описание процесса настройки, запуска и прочая полезная информация о проекте.
- Состав проекта. Используемые решения для backend:
``` 
Django/DRF - Фреймворк для создания веб-API.
Postgresql - Отвечает за базу данных.
Swagger (drf-spectacular) -  Документирование API.
```
- Тестирование:
``` 
pytest-cov - анализ покрытия тестами проекта
pytest-django - набор полезных инструментов для тестирования приложений и проектов Django.
```
- В комплекте с проектом собраны необходимые файлы для создания 3х контейнеров: backend, postgres, nginx.
```
docker-compose.yml - файл с описанием конфигурации для развертывания приложения 
Dockerfile с набором инструкций для образа nginx  
Dockerfile с набором инструкций для образа приложения
nginx.conf - конфигурационный файл nginx
```
- Контейнеры объединяются в сеть, которые работают в связке:
```
Nginx работает в качестве proxy-http для пересылки динамических запросов к Django или возвращая   
статические html файлы.
PostgreSQL запускается до Django.
Django запускается через Gunicorn.
```
- У приложения 2 env файла для тестирования из python и для сборки контейнеров:
```
PROJECT_HOST= адрес хоста
Django_Secret= ваш секретный ключ
DEBUG= режим дебага 
POSTGRES_NAME= имя базы postgresql
POSTGRES_USER= имя пользователя postgresql
POSTGRES_PASSWORD= пароль для подключения к postgresql
POSTGRES_HOST= адрес дата базы
POSTGRES_PORT= порт для подключения к базе

```
- Данное приложение не требует настроек settings.py
- Для работы с контейнерами потребуется установленный Docker Desktop.

- Необходимые файлы для сборки 3х контейнеров уже настроены.  
Практически полное описание Dockerfile, docker-compose и т.п. в моём репозитории  
учебного проекта [Django_docker_compose](https://github.com/Alonsole/Django_docker_compose)

## Инструкция по запуску приложения:
Заполнить 2 файла (.env и .env.compose)   
Миграции и Сборка статики уже настроена  
```
$ docker-compose -f docker-compose.prod.yml up -d --build
```
## Если потребуется удалить:
```
$ docker-compose -f docker-compose.prod.yml down -v
```
## Доступные маршруты:
```
http://localhost/
http://localhost/task/
http://localhost/tags/
http://localhost/admin/login/?next=/admin/
http://localhost/docs/
http://localhost/schema/
```
## Запуск и тесты
- Для тестов:
```
python manage.py runserver 
```
- Контейнеры: 
Запуск через приложение Docker Desktop   
или 
```
docker-compose -f docker-compose.prod.yml up -d
```
- Варианты тестов:
```
tests.py (Запущенный экземпляр python manage.py runserver)
```
Через REST Client - файл requests-examples.http   
Можно тестировать из Swagger http://localhost/docs/

- Охват тестов:
```
pytest --cov=.
```
```
Name                         Stmts   Miss  Cover
------------------------------------------------
prog_task_list\__init__.py       0      0   100%
prog_task_list\admin.py          8      0   100%
prog_task_list\apps.py           4      0   100%
prog_task_list\models.py        16      0   100%
------------------------------------------------
TOTAL                           28      0   100%
```
- Исправить/дополнить охват тестов:  
Отредактируйте файл:
```
.coveragerc
```
## Сборка произведена в Windows  

