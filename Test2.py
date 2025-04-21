from .Test1 import greeting

def test_default():
    assert greeting() == "Welcome, Master"

def test_name():
    assert greeting("John Doe") == "Welcome, John Doe"

def test_argunents():
    for name in ["AG", "John Doe", "Chen Daoxuan", "Ken", "Eiji"]:
        assert greeting(name) == f"Welcome, {name}"