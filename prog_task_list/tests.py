import pytest
from rest_framework.test import APIClient


@pytest.fixture
def client():
    """Фикстура для клиента"""
    return APIClient()


test_url_tags = '/tags/'
test_url_task = '/task/'


@pytest.mark.django_db
def test_post_tags(client):
    """
    Создание тестовых Тегов в Дата базу
    """
    for i in range(1, 11):
        tag_i = f"Тестовый Тег{i}!"
        data = {'name': tag_i}

        response = client.post(
            test_url_tags,
            data=data
        )
        assert response.status_code == 201
        check_tags_base = response.json()
        assert check_tags_base['name'] == data['name']


@pytest.mark.django_db
def test_post_task(client):
    """
    Создание тестового Тега в Дата базу и вносим тестовую задачу
    """
    data = {'name': 'Тестовый Тег'}
    tag_response = client.post(
        test_url_tags,
        data=data
    )

    tag_id = tag_response.data["id"]

    task_data = {
        "title": "Привет, это тестовая задача",
        "description": "Описание тестовой задача",
        "created_at": "2024-12-12T19:32:56.014709Z",
        "tags": [tag_id]
    }

    response = client.post(
        test_url_task,
        data=task_data
    )

    assert response.status_code == 201
    check_task_base = response.json()
    assert check_task_base['title'] == task_data['title']

#
