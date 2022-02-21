from django.test import TestCase
from django.urls import reverse
from shops.models import Shop
from users.models import User


class CreateProductTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )
        cls.shop = Shop.objects.create(
            name='Тестовый магазин'
        )

    def test_create_product_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/shops/product/')
        self.assertEqual(response.status_code, 200)

    def test_create_product_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('create_product'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/create_product.html')

    def test_create_product_was_created_product(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('create_product'),
            data={
                'shop': 1,
                'name': 'Тестовый товар',
                'description': 'Тестирование товара',
                'price': '1000',
                'quantity': '10',
            },
        )
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовый товар')

    def test_create_product_not_was_created_product(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('create_product'),
            data={
                'name': 'Тестовый товар',
                'description': 'Тестирование товара',
                'price': '1000',
                'quantity': '10'
            },
        )
        self.assertEqual(response.status_code, 200)
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Тестовый товар')
