from django.contrib.auth import get_user_model
from django.shortcuts import reverse
from django.test import TestCase


class RegisterTest(TestCase):
    def test_register_exists_at_desired_location(self):
        response = self.client.get('/users/register/')
        self.assertEqual(response.status_code, 200)

    def test_register_uses_correct_template(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/register.html')

    def test_register_form(self):
        response = self.client.post(
            reverse('register'), data={
                'username': 'IgorSemenov',
                'password1': 'qwertyu1234',
                'password2': 'qwertyu1234',
                'first_name': 'Igor',
                'last_name': 'Semenov',
                'email': 'test@mail.ru',
                'phone': '89131113333',
            },
        )
        self.assertEqual(response.status_code, 302)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)

    def test_not_register_form(self):
        response = self.client.post(
            reverse('register'),
            data={
                'username': 'IgorSemenov',
                'password1': 'qwertyu1234',
                'password2': 'qwertyu123',
                'first_name': 'Igor',
                'last_name': 'Semenov',
                'email': 'test@mail.ru',
                'phone': '89131113333',
                'about_me': 'Python разработка'
            },
        )
        self.assertEqual(response.status_code, 200)
        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 0)
