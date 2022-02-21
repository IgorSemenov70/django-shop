from django.test import TestCase
from django.urls import reverse
from users.models import User


class ProductListByShopTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            password='secret',
        )

    def test_product_statistics_exists_at_desired_location(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(f'/shops/product_statistics/')
        self.assertEqual(response.status_code, 200)

    def test_product_statistics_uses_correct_template(self):
        self.client.login(username='testuser', password='secret')
        response = self.client.get(reverse('product_statistics'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shops/product_statistics.html')
