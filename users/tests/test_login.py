from django.shortcuts import reverse
from django.test import TestCase
from users.models import User


class LoginTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_login_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_user_was_authenticated(self):
        response = self.client.post('/users/login/', {'username': 'testuser', 'password': 'secret'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_user_not_was_authenticated(self):
        response = self.client.post('/users/login/', {'username': 'anonuser', 'password': 'secret'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
