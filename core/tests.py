from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class HomePageTestCase(TestCase):

    
    def test_home_page_accessible_by_authenticated_user(self):
        user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')

        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_home_page_redirects_for_unauthenticated_user(self):

        login_url = reverse('accounts:login_form')
        response = self.client.get('/')
        self.assertRedirects(response, f'{login_url}?next=/')