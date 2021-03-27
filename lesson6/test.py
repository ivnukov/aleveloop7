from unittest import TestCase, skip, mock

from lesson6.testing import User


class UserTest(TestCase):

    def setUp(self) -> None:
        self.user = User('Test Userovich', 21)
        self.new_name = 'Ivan Ivanov'

    @mock.patch('lesson6.testing.User.calculate_year_of_birth', return_value='11')
    def test_calculate_year_of_birth(self):
        result = self.user.calculate_year_of_birth()
        self.assertEqual(result, 2000)

    def test_change_name_success(self):
        self.user.change_name(self.new_name)
        self.assertEqual(self.user.name, self.new_name)

    def test_change_name_same_name_cause_error(self):
        self.assertRaises(ValueError,
                          self.user.change_name,
                          'Test Userovich')
