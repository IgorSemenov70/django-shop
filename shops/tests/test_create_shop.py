from django.test import TestCase
from django.urls import reverse
from users.models import User


class CreateShopTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_create_shop_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/shops/create_shop/')
        self.assertEqual(response.status_code, 200)

    def test_create_shop_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('create_shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/create_shop.html')

    def test_create_shop_was_created_shop(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('create_shop'), data={'name': 'Тестовый магазин'})
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовый магазин')

    def test_create_shop_not_was_created_shop(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('create_shop'), data={})
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Тестовый магазин')