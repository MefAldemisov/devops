from app_python.main import get_time


def test_get_time():
    moscow_time = get_time("Europe/Moscow")
    vladivostok_time = get_time("Asia/Vladivostok")
    assert moscow_time != vladivostok_time


def test_get_time_at(client):
    response = client.get("/time/Europe/Moscow")
    data = response.data.decode("utf-8")
    assert "Moscow" in data
    assert "Europe" not in data
    assert "Return" in data

def test_404(client):
    not_found = client.get("/time/Eurape/Moscow")
    assert not_found.status_code == 404
    print("NF", not_found.data)
    assert "time zone not found" in not_found.data.decode("utf-8")
    response = client.get("/Moscow")
    assert response.status_code == 404


def test_index(client):
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "Europe/Moscow" in data
    assert "Asia/Vladivostok" in data
