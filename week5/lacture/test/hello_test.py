from hello import hello


def test_hello_default():
    assert hello() == "Hello, Wold" # Intentional typo here

def test_hello_name():
    assert hello("Alice") == "Hello, Alice"
