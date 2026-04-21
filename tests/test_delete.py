from api_client import YaDiskClient


def test_delete_folder():
    folder_name = "folder_to_delete"

    YaDiskClient.put("/resources", params={"path": folder_name})
    resp = YaDiskClient.delete("/resources", params={"path": folder_name, "permanently": True})
    assert resp.status_code == 204

    check = YaDiskClient.get("/resources", params={"path": folder_name})
    assert check.status_code == 404
    print(f"OK: папка {folder_name} удалена")


def test_delete_nonexistent_folder():
    resp = YaDiskClient.delete("/resources", params={"path": "/nonexistent_12345", "permanently": True})
    assert resp.status_code == 404
    print("OK: 404 при удалении несуществующей папки")