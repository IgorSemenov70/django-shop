from django.test import TestCase
from django.urls import reverse
from shops.models import Shop, Product
from users.models import User


class CartTest(TestCase):
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

    def test_cart_detail_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get('/cart/cart_detail/')
        self.assertEqual(response.status_code, 200)

    def test_cart_detail_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'cart/cart_detail.html')

    def test_adding_an_product_to_the_cart(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('cart_add', kwargs={'pk': self.product.pk}),
            data={
                'quantity': '2'
            })
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.product.name)

    def test_remove_an_product_from_the_cart(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('cart_add', kwargs={'pk': self.product.pk}),
            data={
                'quantity': '2'
            })
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('cart_remove', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 302)
        response = self.client.get(reverse('cart_detail'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, self.product.name)
