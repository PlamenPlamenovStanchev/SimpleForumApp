from django.core.exceptions import ValidationError
from django.test import TestCase

from posts.validators import BadLanguageValidator


class TestBadLanguageValidator(TestCase):
    def setUp(self):
        self.bad_words = [
            'fuck', 'bitch', 'shit', 'whore', 'slut', 'ass', 'nigga'
        ]
        self.validator = BadLanguageValidator()


    def test__validate_clean_message__expect_success(self):
        self.validator("Clean message")

    def test__validate_explicit_content_message__expect_validation_error(self):
        with self.assertRaises(ValidationError) as ve:
            self.validator(self.bad_words[0] + 'something')

            self.assertTrue(str(ve))