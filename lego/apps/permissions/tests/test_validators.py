from django.core.exceptions import ValidationError
from django.test import TestCase

from lego.apps.permissions.validators import KeywordPermissionValidator


class KeywordPermissionValidatorTestCase(TestCase):
    def test_regex_validator_non_letters(self):
        validator = KeywordPermissionValidator()
        self.assertRaises(ValidationError, validator.__call__, '/1234/')

    def test_regex_validator_valid(self):
        validator = KeywordPermissionValidator()
        validator.__call__('/sudo/')

    def test_regex_validator_ending_slash(self):
        validator = KeywordPermissionValidator()
        self.assertRaises(ValidationError, validator.__call__, '/sudo')

    def test_regex_validator_starting_slash(self):
        validator = KeywordPermissionValidator()
        self.assertRaises(ValidationError, validator.__call__, 'sudo/')

    def test_regex_validator_double_start_slash(self):
        """
        Two slashes in the beginning of the string is not allowed.
        """
        validator = KeywordPermissionValidator()
        self.assertRaises(ValidationError, validator.__call__, '//sudo/')
