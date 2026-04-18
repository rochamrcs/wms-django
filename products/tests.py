from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product
from django.urls import reverse


class ProductsPageTestCase(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    
    def test_home_page_accessible_by_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/products/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products.html')


    def test_products_page_redirects_for_unauthenticated_user(self):

        login_url = reverse('accounts:login_form')
        response = self.client.get('/')
        self.assertRedirects(response, f'{login_url}?next=/')

    
    def test_new_product_page_accessible_by_authenticated_user(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/products/new_product/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_product.html')


    def test_new_product_page_redirects_for_unauthenticated_user(self):
        login_url = reverse('accounts:login_form')
        response = self.client.get('/products/new_product/')
        self.assertRedirects(response, f'{login_url}?next=/products/new_product/')

    
    def test_new_product_form_submission(self):
        self.client.login(username='testuser', password='testpassword')

        form_data = {
            'name': 'Test Product',
            'product_code': 'TP001',
            'umb': 'UN',
            'product_type': '3',
        }
        response = self.client.post('/products/new_product/', data=form_data)
        self.assertRedirects(response, '/products/')

    
    def test_product_created_in_database(self):
        self.client.login(username='testuser', password='testpassword')

        self.client.post('/products/new_product/', data={
            'name': 'Produto DB',
            'product_code': 'DB001',
            'umb': 'UN',
            'product_type': '1',
        })

        self.assertEqual(Product.objects.count(), 1)


    def test_products_search_by_name(self):
        self.client.login(username='testuser', password='testpassword')

        Product.objects.create(name='Parafuso', product_code='P001', product_type='1')

        response = self.client.get('/products/?q=Parafuso')
        self.assertContains(response, 'Parafuso')


    def test_products_search_by_code(self):
        self.client.login(username='testuser', password='testpassword')

        Product.objects.create(name='Porca', product_code='PX01', product_type='1')

        response = self.client.get('/products/?q=PX01')
        self.assertContains(response, 'Porca')

    
    def test_filter_active_products(self):
        self.client.login(username='testuser', password='testpassword')

        Product.objects.create(name='Ativo', product_code='A1', status=True, product_type='1')
        Product.objects.create(name='Inativo', product_code='I1', status=False, product_type='1')

        response = self.client.get('/products/?status=ativo')

        products = response.context['products_list']

        self.assertEqual(products.count(), 1)
        self.assertEqual(products.first().name, 'Ativo')


    def test_filter_inactive_products(self):
        self.client.login(username='testuser', password='testpassword')

        Product.objects.create(name='Ativo', product_code='A1', status=True, product_type='1')
        Product.objects.create(name='Inativo', product_code='I1', status=False, product_type='1')

        response = self.client.get('/products/?status=inativo')

        products = response.context['products_list']

        self.assertEqual(products.count(), 1)
        self.assertEqual(products.first().name, 'Inativo')


    def test_new_product_invalid_form(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post('/products/new_product/', data={})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'new_product.html')
    

    def test_product_code_must_be_unique(self):
        self.client.login(username='testuser', password='testpassword')

        Product.objects.create(name='Produto 1', product_code='DUP', product_type='1')

        response = self.client.post('/products/new_product/', data={
            'name': 'Produto 2',
            'product_code': 'DUP',
            'umb': 'UN',
            'product_type': '1',
        })

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'error')

    
    def test_change_status_route_return_status_code_302_and_redirects(self):
        self.client.login(username='testuser', password='testpassword')

        product = Product.objects.create(name='Produto Status', product_code='PS001', status=True, product_type='1')

        response = self.client.post(f'/products/{product.id}/change_status/')

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/products/')


    def test_change_status_was_toggled(self):
        self.client.login(username='testuser', password='testpassword')

        product = Product.objects.create(name='Produto Status', product_code='PS001', status=True, product_type='1')

        response = self.client.post(f'/products/{product.id}/change_status/')

        product.refresh_from_db()

        self.assertFalse(product.status)

    
    def test_change_status_return_404_invalid_product(self):
        self.client.login(username='testuser', password='testpassword')

        response = self.client.post(f'/products/{99}/change_status/')

        self.assertEqual(response.status_code, 404)


    def test_change_status_page_redirects_for_unauthenticated_user(self):

        login_url = reverse('accounts:login_form')

        product = Product.objects.create(name='Produto Status', product_code='PS001', status=True, product_type='1')

        response = self.client.post(f'/products/{product.id}/change_status/')

        self.assertRedirects(response, f'{login_url}?next=/products/{product.id}/change_status/')


    def test_change_status_redirects_when_method_is_not_post(self):

        self.client.login(username='testuser', password='testpassword')

        product = Product.objects.create(name='Produto Status', product_code='PS001', status=True, product_type='1')

        response = self.client.get(f'/products/{product.id}/change_status/')

        self.assertRedirects(response, '/products/')