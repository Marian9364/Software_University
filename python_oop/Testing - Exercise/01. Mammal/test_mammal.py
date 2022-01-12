from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):
    name = "Name"
    mammal_type = "Type"
    sound = "Sound"
    kingdom = "animals"

    def setUp(self) -> None:
        self.mammal = Mammal(self.name, self.mammal_type, self.sound)

    def test_mammal_initialization(self):
        self.assertEqual(self.name, self.mammal.name)
        self.assertEqual(self.mammal_type, self.mammal.type)
        self.assertEqual(self.sound, self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_should_return_sound_as_a_string(self):
        expected = f"{self.mammal.name} makes {self.mammal.sound}"
        actual = self.mammal.make_sound()
        self.assertEqual(expected, actual)

    def test_get_kingdom__should_return_kingdom_as_string(self):
        expected = "animals"
        actual = self.mammal.get_kingdom()
        self.assertEqual(expected, actual)

    def test_info__should_return_info_about_name_and_type(self):
        expected = f"{self.mammal.name} is of type {self.mammal.type}"
        actual = self.mammal.info()
        self.assertEqual(expected, actual)


if __name__ == "__Main__":
    main()
