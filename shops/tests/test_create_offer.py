from django.test import TestCase
from django.urls import reverse
from users.models import User


class CreateOfferTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_create_offer_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/shops/offer/')
        self.assertEqual(response.status_code, 200)

    def test_create_offer_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('create_offer'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/create_offer.html')

    def test_create_offer_was_created_offer(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('create_offer'),
            data={
                'name': 'Тестовое предложение',
                'description': 'Тестирование предложений',
            },
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('personal-account'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовое предложение')

    def test_create_offer_not_was_created_offer(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('create_offer'),
            data={
                'description': 'Тестирование предложений',
            },
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('personal-account'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Тестирование предложений')