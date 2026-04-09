from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class ProductsPageTestCase(TestCase):

    
    def test_home_page_accessible_by_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')


    def test_products_page_redirects_for_unauthenticated_user(self):

        login_url = reverse('accounts:login_form')
        response = self.client.get('/')
        self.assertRedirects(response, f'{login_url}?next=/')

    
    def test_new_product_page_accessible_by_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/products/new_product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_product.html')


    def test_new_product_page_redirects_for_unauthenticated_user(self):
        login_url = reverse('accounts:login_form')
        response = self.client.get('/products/new_product/')
        self.assertRedirects(response, f'{login_url}?next=/products/new_product/')

    
    def test_new_product_form_submission(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        form_data = {
            'name': 'Test Product',
            'product_code': 'TP001',
            'umb': 'UN',
            'product_type': '3',
        }
        response = self.client.post('/products/new_product/', data=form_data)
        self.assertRedirects(response, '/products/')
