import unittest

from solutions.py_intro.func_and_class import greet, Person


class TestGreetFunction(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet("Alice"), "Hello, Alice!")
        self.assertEqual(greet("Bob"), "Hello, Bob!")
        self.assertNotEqual(greet("Alice"), "Hello, Bob!")

class TestPersonClass(unittest.TestCase):
    def test_person_initialization(self):
        person = Person("Charlie", 30)
        self.assertEqual(person.name, "Charlie")
        self.assertEqual(person.age, 30)

    def test_introduce(self):
        person = Person("Diana", 25)
        self.assertEqual(person.introduce(), "My name is Diana and I am 25 years old.")



if __name__ == '__main__':
    unittest.main()
