from django.test import TestCase
from django.urls import reverse
from shops.models import Product, Shop
from users.models import User


class ShopsAndProductListTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )
        shop = Shop.objects.create(
            name='Тестовый магазин'
        )
        cls.product = Product.objects.create(
            shop=shop,
            name='Тестовый продукт',
            description='Тестирование',
            price='1000',
            quantity='10',
        )

    def test_shops_and_product_list_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/shops/main_page/')
        self.assertEqual(response.status_code, 200)

    def test_shops_and_product_list_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/shops_and_product_list.html')

    def test_shops_and_product_list_published_shop_and_product(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('shops_and_product_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовый магазин')
        self.assertContains(response, 'Тестовый продукт')
