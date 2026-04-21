import requests
from api_client import YaDiskClient

def test_copy_folder():
    source = "test_api_folder"
    dest = "test_api_folder_copy"

    YaDiskClient.put("/resources", params={"path": source})
    resp = YaDiskClient.post("/resources/copy", params={"from": source, "path": dest})
    assert resp.status_code in [201, 202]
    print(f"OK: папка скопирована {source} -> {dest}")

    YaDiskClient.delete("/resources", params={"path": dest, "permanently": True})
    YaDiskClient.delete("/resources", params={"path": source, "permanently": True})

def test_upload_from_url():
    resp = YaDiskClient.post("/resources/upload",
                             params={"path": "test.pdf",
                                     "url": "https://www.w3.org/WAI/er/tests/xhtml/testfiles/resources/pdf/dummy.pdf"})
    assert resp.status_code == 202
    print("OK: загрузка по URL запущена")