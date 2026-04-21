from api_client import YaDiskClient


def test_create_folder_put():
    folder_name = "put_test_folder"
    resp = YaDiskClient.put("/resources", params={"path": folder_name})
    assert resp.status_code == 201

    check = YaDiskClient.get("/resources", params={"path": folder_name})
    assert check.status_code == 200

    YaDiskClient.delete("/resources", params={"path": folder_name, "permanently": True})
    print(f"OK: папка {folder_name} создана и удалена")


def test_create_existing_folder():
    folder_name = "existing_folder"

    YaDiskClient.put("/resources", params={"path": folder_name})
    resp = YaDiskClient.put("/resources", params={"path": folder_name})
    assert resp.status_code in [409, 423]

    YaDiskClient.delete("/resources", params={"path": folder_name, "permanently": True})
    print("OK: при создании существующей папки ошибка")