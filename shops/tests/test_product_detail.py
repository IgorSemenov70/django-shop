from django.urls import reverse
from django.test import TestCase
from users.models import User
from shops.models import Product, Shop


class ProductDetailTest(TestCase):
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

    def test_product_detail_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(f'/shops/product_detail/{self.product.pk}/')
        self.assertEqual(response.status_code, 200)

    def test_product_detail_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('product_detail', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/product_detail.html')

    def test_product_detail_published_posts(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('product_detail', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовый продукт')