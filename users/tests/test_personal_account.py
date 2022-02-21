from django.test import TestCase
from django.shortcuts import reverse
from users.models import User


class PersonalAccountTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
            email='test@mail.ru',
            phone='89131113322',
        )

    def test_personal_account_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/users/personal_account/')
        self.assertEqual(response.status_code, 200)

    def test_personal_account_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('personal-account'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/personal_account.html')

    def test_personal_account_published_info(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('personal-account'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')
