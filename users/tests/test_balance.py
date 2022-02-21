from django.shortcuts import reverse
from django.test import TestCase
from users.models import User


class BalanceTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_balance_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/users/balance/')
        self.assertEqual(response.status_code, 200)

    def test_balance_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('balance'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/balance.html')

    def test_balance_was_changed(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('balance'), data={'balance': 1000})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('balance'))
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username=self.user)
        self.assertEqual(user.balance, 1000)

    def test_balance_not_was_changed(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('balance'), data={'balance': 10000000000})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('balance'))
        self.assertEqual(response.status_code, 200)
        user = User.objects.get(username=self.user)
        self.assertNotEqual(user.balance, 10000000000)
