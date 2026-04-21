import pytest
from api_client import YaDiskClient


@pytest.fixture
def test_folder():
    folder_name = "test_api_folder"
    YaDiskClient.put("/resources", params={"path": folder_name})
    yield folder_name
    YaDiskClient.delete("/resources", params={"path": folder_name, "permanently": True})