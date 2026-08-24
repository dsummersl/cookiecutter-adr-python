from {{cookiecutter.package_name}}.hello import world


def test_world():
    assert world() == "hello world"
