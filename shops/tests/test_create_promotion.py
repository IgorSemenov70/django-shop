from django.test import TestCase
from django.urls import reverse
from users.models import User


class CreatePromotionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_create_promotion_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/shops/promotion/')
        self.assertEqual(response.status_code, 200)

    def test_create_promotion_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('create_promotion'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/create_promotion.html')

    def test_create_promotion_was_created_offer(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('create_promotion'),
            data={
                'name': 'Тестовая акция',
                'description': 'Тестирование акций',
            },
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('personal-account'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая акция')

    def test_create_promotion_not_was_created_offer(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('create_promotion'),
            data={
                'description': 'Тестирование акций',
            },
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('personal-account'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Тестирование акций')