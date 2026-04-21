import pytest
from api_client import YaDiskClient


def test_get_folder_contents(test_folder):
    """GET /resources: получить содержимое папки"""
    resp = YaDiskClient.get("/resources", params={"path": test_folder})
    assert resp.status_code == 200
    assert "_embedded" in resp.json()
    print(f"✅ Папка '{test_folder}' успешно получена")


def test_get_metadata_has_required_fields():
    """GET /resources: проверка обязательных полей в ответе"""
    resp = YaDiskClient.get("/resources", params={"path": "/"})
    assert resp.status_code == 200
    data = resp.json()
    
    assert "name" in data, "Поле 'name' отсутствует"
    assert "created" in data, "Поле 'created' отсутствует"
    assert "modified" in data, "Поле 'modified' отсутствует"
    assert "path" in data, "Поле 'path' отсутствует"
    print(f"✅ Все обязательные поля присутствуют")


@pytest.mark.parametrize("path,expected_status", [
    ("/", 200),                     # Корневая папка
    ("/nonexistent_folder_12345", 404),  # Несуществующая папка
])
def test_get_different_paths(path, expected_status):
    """GET /resources: параметризованный тест разных путей"""
    resp = YaDiskClient.get("/resources", params={"path": path})
    assert resp.status_code == expected_status
    print(f"✅ Путь '{path}' вернул статус {expected_status}")
