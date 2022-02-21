from django.test import TestCase
from django.shortcuts import reverse
from users.models import User


class LogoutTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_logout_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/users/logout/')
        self.assertEqual(response.status_code, 302)

    def test_logout_uses_correct_url_name(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

    def test_logout_user_logged_out(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post('/users/logout/', data={'username': 'testuser', 'password': 'secret'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_logout_has_the_user_logged_out(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Выйти из аккаунта')
        self.client.logout()
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Войти')