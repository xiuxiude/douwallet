from tests import utils


@utils.with_client
def test_home(client):
    """douwallet.views.home:home"""
    response = client.get("/")
    utils.assert_200(response)
    utils.assert_responded(response, "It works.")
