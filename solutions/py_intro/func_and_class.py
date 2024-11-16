def greet(name: str) -> str:
    """
    Returns a greeting message.
    :param name: the name to greet
    :return:
        str: a greeting message
    """
    return f"Hello, {name}!"


class Person:
    """
    Represents a person with a name and age.
    """
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self) -> str:
        return f"My name is {self.name} and I am {self.age} years old."
