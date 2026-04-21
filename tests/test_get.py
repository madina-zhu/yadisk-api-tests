import pytest
from api_client import YaDiskClient


def test_get_folder_contents(test_folder):
    resp = YaDiskClient.get("/resources", params={"path": test_folder})
    assert resp.status_code == 200
    assert "_embedded" in resp.json()
    print(f"OK: папка {test_folder} получена")


def test_get_metadata_has_required_fields():
    resp = YaDiskClient.get("/resources", params={"path": "/"})
    assert resp.status_code == 200
    data = resp.json()

    assert "name" in data, "Поле name отсутствует"
    assert "created" in data, "Поле created отсутствует"
    assert "modified" in data, "Поле modified отсутствует"
    assert "path" in data, "Поле path отсутствует"
    print("OK: метаданные содержат все поля")


@pytest.mark.parametrize("path,expected_status", [
    ("/", 200),
    ("/nonexistent_folder_12345", 404),
])
def test_get_different_paths(path, expected_status):
    resp = YaDiskClient.get("/resources", params={"path": path})
    assert resp.status_code == expected_status
    print(f"OK: путь {path} вернул {expected_status}")