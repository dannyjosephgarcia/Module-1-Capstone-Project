import unittest
from functions.misc_functions import MiscFunctions

TEST_DICTIONARY = {'fruit1': 'apples',
                   'fruit2': 'bananas'}


class TestMiscFunctions(unittest.TestCase):
    def setUp(self):
        self.misc_functions = MiscFunctions()

    def test_get_all_dictionary_keys(self):
        keys_list = self.misc_functions.get_all_dictionary_keys(TEST_DICTIONARY)
        self.assertEqual(['fruit1', 'fruit2'], keys_list)

    def test_get_all_dictionary_values(self):
        # TODO: Implement the remainder of this unittest
        # ================================ YOUR CODE HERE ============================== #
        pass

    def test_get_all_dictionary_pairs(self):
        # TODO: Implement the remainder of this unittest
        # ================================ YOUR CODE HERE ============================== #
        pass

    def test_get_number_give_modulus(self):
        # TODO: Implement the remainder of this unittest
        # ================================ YOUR CODE HERE ============================== #
        pass


if __name__ == "__main__":
    unittest.main()
