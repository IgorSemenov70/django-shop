from django.test import TestCase
from django.urls import reverse
from orders.models import OrderItem
from shops.models import Shop, Product
from users.models import User


class OrderCreatedTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
            first_name='Игорь',
            last_name='Семёнов',
            email='test@mail.ru',
            address='ул. Тестовая 4 кв.5',
            postal_code='345654',
            city='Томск',
            balance='10000.00'
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

    def test_order_created_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(reverse('order_created'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_created.html')
        self.assertContains(response, 'Спасибо за заказ')

    def test_order_item_created(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('cart_add', kwargs={'pk': self.product.pk}),
            data={
                'quantity': '2'
            })
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('order_created'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(OrderItem.objects.all().count(), 1)

    def test_fail_order_item_created(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.post(
            reverse('cart_add', kwargs={'pk': self.product.pk}),
            data={
                'quantity': '15'
            })
        self.assertEqual(response.status_code, 302)
        response = self.client.post(reverse('order_created'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(OrderItem.objects.all().count(), 0)
