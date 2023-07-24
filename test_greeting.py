from greeting import greeting

def test_hello_world_output():
    output = greeting()
    assert output == "Hello world!"