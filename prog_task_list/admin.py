from django.contrib import admin
from prog_task_list.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'due_date', 'is_completed', 'created_at']


@admin.register(Tag)
class TagsAdmin(admin.ModelAdmin):
    list_display = ['name']
