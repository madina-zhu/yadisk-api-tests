from api_client import YaDiskClient


def test_delete_folder():
    """DELETE /resources: удалить папку"""
    folder_name = "folder_to_delete"
    
    # Создаем папку
    YaDiskClient.put("/resources", params={"path": folder_name})
    
    # Удаляем
    resp = YaDiskClient.delete("/resources", params={"path": folder_name, "permanently": True})
    assert resp.status_code == 204
    print(f"✅ Папка '{folder_name}' удалена")
    
    # Проверяем, что папки больше нет
    check = YaDiskClient.get("/resources", params={"path": folder_name})
    assert check.status_code == 404
    print("✅ Проверка: папка действительно удалена")


def test_delete_nonexistent_folder():
    """DELETE /resources: ошибка при удалении несуществующей папки"""
    resp = YaDiskClient.delete("/resources", params={"path": "/nonexistent_12345", "permanently": True})
    assert resp.status_code == 404
    print("✅ Несуществующая папка вернула 404")
