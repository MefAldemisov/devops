"""
This module is responsible the testing of the requests in the
`app_python`: 404, init and the response pages
"""


class Requester:
    """
    Class, which wraps the request and takes the required
    data from it
    """

    def __init__(self, client, request: str):
        response = client.get(request)
        self.status = response.status_code
        self.data = response.data.decode("utf-8")

    def response_has(self, substring: str) -> bool:
        """
        Checks if the resulted webpage includes the given substring
        :param substring: the string, which will be searched in the response
        :return: boolean value, if the substring is in the response
        """
        return substring in self.data

    def get_status(self) -> int:
        """
        Getter for the response status
        :return:
        """
        return self.status


def test_city_name_in_response(client):
    """
    Test for `main.get_time_at` function.
    Checks if the city-based response includes the name of the city
    :param client: client for a Flask app
    """
    assert Requester(client, "/time/Europe/Moscow").response_has("Moscow")


def test_region_name_not_in_response(client):
    """
    Test for `main.get_time_at` function.
    Validates that the city-based response doesn't include the region
    :param client: client for a Flask app
    """
    assert not Requester(client, "/time/Europe/Moscow").response_has("Europe")


def test_link_in_response(client):
    """
    Test for `main.get_time_at` function.
    Checks that it is possible to return to the main page from the response
    :param client: client for a Flask app
    """
    assert Requester(client, "/time/Europe/Moscow").response_has('<a href="/">')


def test_wrong_path_msg(client):
    """
    Validation of the explanation of the wrong API
    :param client: client for a Flask app
    """
    assert Requester(client, "/time/Eurape/Moscow").response_has("time zone not found")


def test_wrong_path_404(client):
    """
    Validation of the error in case of wrong API
    :param client: client for a Flask app
    """
    assert Requester(client, "/Moscow").get_status() == 404


def test_index_has_cities(client):
    """
    Test for `main.get_list_of_time_zones`
    :param client: client for a Flask app
    """
    assert Requester(client, "/").response_has("Asia/Vladivostok")
