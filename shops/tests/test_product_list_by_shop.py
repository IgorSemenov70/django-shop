from django.test import TestCase
from django.urls import reverse
from shops.models import Product, Shop
from users.models import User


class ProductListByShopTest(TestCase):
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

    def test_product_list_by_shop_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(f'/shops/main_page/{self.product.shop.pk}')
        self.assertEqual(response.status_code, 301)

    def test_product_list_by_shop_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('product_list_by_shop', kwargs={'pk': self.product.shop.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/shops_and_product_list.html')

    def test_product_list_by_shop_published_product_by_shop(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('product_list_by_shop', kwargs={'pk': self.product.shop.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Товары магазина: Тестовый магазин')
