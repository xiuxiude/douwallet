import functools

from douwallet.app import create_app
from nose.tools import assert_equal, assert_in


def with_client(wrapped):
    """The testing context of app."""
    def wrapper():
        app = create_app()
        app.config["TESTING"] = True
        return wrapped(app.test_client())
    return functools.update_wrapper(wrapper, wrapped)


def assert_status(response, status):
    assert_equal(response.status_code, status)


assert_200 = functools.partial(assert_status, status=200)
assert_400 = functools.partial(assert_status, status=400)
assert_401 = functools.partial(assert_status, status=401)
assert_403 = functools.partial(assert_status, status=403)
assert_404 = functools.partial(assert_status, status=404)
assert_405 = functools.partial(assert_status, status=405)


def assert_responded(response, fragment, partial=False):
    if partial:
        assert_in(fragment, response.data)
    else:
        assert_equal(response.data, fragment)
