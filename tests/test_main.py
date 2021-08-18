from app_python.main import get_time


def test_get_time():
    """
    Test for `main.get_time()` function
    """
    moscow_time = get_time("Europe/Moscow")
    vladivostok_time = get_time("Asia/Vladivostok")
    assert moscow_time != vladivostok_time


def test_get_time_at(client):
    """
    Test for `main.get_time_at` function
    :param client: client for a Flask app
    """
    response = client.get("/time/Europe/Moscow")
    data = response.data.decode("utf-8")
    assert "Moscow" in data
    assert "Europe" not in data
    assert "Return" in data


def test_404(client):
    """
    Test for `main.page_not_found` and `main.get_time_at` functions.
    The goal of the check is the validation of the 404 error.
    :param client: client for a Flask app
    """
    not_found = client.get("/time/Eurape/Moscow")
    assert not_found.status_code == 404
    print("NF", not_found.data)
    assert "time zone not found" in not_found.data.decode("utf-8")
    response = client.get("/Moscow")
    assert response.status_code == 404


def test_index(client):
    """
    Test for `main.get_list_of_time_zones`
    :param client: client for a Flask app
    """
    response = client.get("/")
    data = response.data.decode("utf-8")
    assert "Europe/Moscow" in data
    assert "Asia/Vladivostok" in data
