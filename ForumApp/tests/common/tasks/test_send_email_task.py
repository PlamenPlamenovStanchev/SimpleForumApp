from unittest.mock import patch

from django.test import TestCase

from common.tasks import _send_mail


class TestSendEmailTask(TestCase):

    @patch('common.tasks.send_email')
    async def test__send_email__calls_django_send_mail_func(self, mock_django_send_email):
        await _send_mail(
            subject='TestSubject',
            message='TestMessage',
            from_email='test@test.com',
            recipient_list=['test1@test.com'],
        )

        mock_django_send_email.assert_called_once_with(
            subject='TestSubject',
            message='TestMessage',
            from_email='test@test.com',
            recipient_list=['test1@test.com'],
        )
