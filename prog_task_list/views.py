from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer
from .schema import task_doc, tags_doc


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@task_doc
class TaskViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    queryset = Task.objects.all().order_by('-created_at')  # Сортировка по убыванию даты создания
    serializer_class = TaskSerializer
    pagination_class = CustomPagination



@tags_doc
class TagViewSet(viewsets.ModelViewSet):
    http_method_names = ['get', 'post', 'delete']
    queryset = Tag.objects.all().order_by('name')  # Сортировка по убыванию даты создания
    serializer_class = TagSerializer
    pagination_class = CustomPagination
