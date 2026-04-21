from api_client import YaDiskClient


def test_create_folder_put():
    """PUT /resources: создать новую папку"""
    folder_name = "put_test_folder"
    resp = YaDiskClient.put("/resources", params={"path": folder_name})
    assert resp.status_code == 201
    print(f"✅ Папка '{folder_name}' создана")
    
    # Проверяем, что папка действительно создалась
    check = YaDiskClient.get("/resources", params={"path": folder_name})
    assert check.status_code == 200
    
    # Удаляем
    YaDiskClient.delete("/resources", params={"path": folder_name, "permanently": True})
    print(f"✅ Папка '{folder_name}' удалена")


def test_create_existing_folder():
    """PUT /resources: попытка создать существующую папку"""
    folder_name = "existing_folder"
    # Создаем первый раз
    YaDiskClient.put("/resources", params={"path": folder_name})
    
    # Пытаемся создать второй раз
    resp = YaDiskClient.put("/resources", params={"path": folder_name})
    assert resp.status_code in [409, 423]  # Конфликт или уже существует
    
    # Очистка
    YaDiskClient.delete("/resources", params={"path": folder_name, "permanently": True})
    print("✅ Попытка создать существующую папку вернула ошибку")
