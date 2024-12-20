from drf_spectacular.utils import extend_schema, extend_schema_view, OpenApiResponse

"""#добавляем информацию о каждом методе в документацию Swagger/OpenAPI для Задач
"""
task_doc = extend_schema_view(
    list=extend_schema(
        summary='Получения всех задач',
        description='Эндпоинт для получения всех задач и ДатаБазы.',
    ),
    create=extend_schema(
        summary='Создание новой задачи',
        description='Эндпоинт для создания новой задачи.',
    ),
    retrieve=extend_schema(
        summary='Получение информации о конкретной задаче по № ID',
        description='Эндпоинт для получения задачи по её идентификатору.',
    ),
    partial_update=extend_schema(
        summary='Обновление информации о конкретной задаче по № ID',
        description='Эндпоинт для обновления информации о конкретной задаче по её идентификатору.',
    ),
    destroy=extend_schema(
        summary='Удаление конкретной задачи по № ID',
        description='Эндпоинт для удаления задачи по её идентификатору.',
        responses={
            204: OpenApiResponse(description="Операция по удалению завершена успешно"),
            404: OpenApiResponse(description="Операция не выполнена. Указанного ID нет."),
        }
    ),
)

"""#добавляем информацию о каждом методе в документацию Swagger/OpenAPI для Тегов
"""
tags_doc = extend_schema_view(
    list=extend_schema(
        summary='Получения всех тегов',
        description='Эндпоинт для получения всех тегов и ДатаБазы.',
    ),
    create=extend_schema(
        summary='Создание нового тега',
        description='Эндпоинт для создания нового тега.',
    ),
    retrieve=extend_schema(
        summary='Получение информации о конкретной теге по № ID',
        description='Эндпоинт для получения тега по её идентификатору.',
    ),
    destroy=extend_schema(
        summary='Удаление конкретного тега по № ID',
        description='Эндпоинт для удаления тега по её идентификатору.',
        responses={
            204: OpenApiResponse(description="Операция по удалению завершена успешно"),
            404: OpenApiResponse(description="Операция не выполнена. Указанного ID нет."),
        }
    ),
)