from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Location, LocationStatus, LocationType, Plant, Storage, UnitOfMeasure


class LocationsPageTestCase(TestCase):
	def setUp(self):
		self.user = User.objects.create_user(username='testuser', password='testpassword')
		self.plant = Plant.objects.create(name='Planta Norte')
		self.other_plant = Plant.objects.create(name='Planta Sul')
		self.storage = Storage.objects.create(name='Armazem A', plant=self.plant)
		self.other_storage = Storage.objects.create(name='Armazem B', plant=self.other_plant)
		location_type = LocationType.objects.create(name='Picking')
		self.location = Location.objects.create(
			address='A-01-01', storage=self.storage, capacity=10,
			capacity_unit=UnitOfMeasure.PALLET, location_type=location_type,
		)
		self.blocked_location = Location.objects.create(
			address='B-02-02', storage=self.other_storage, capacity=20,
			capacity_unit=UnitOfMeasure.KILOGRAM, location_type=location_type,
			status=LocationStatus.BLOCKED,
		)

	def test_locations_page_requires_authentication(self):
		response = self.client.get(reverse('wharehouses:locations'))

		self.assertRedirects(response, '/auth/?next=/warehouses/')

	def test_locations_page_lists_location_fields(self):
		self.client.login(username='testuser', password='testpassword')

		response = self.client.get(reverse('wharehouses:locations'))

		self.assertEqual(response.status_code, 200)
		self.assertTemplateUsed(response, 'locations.html')
		self.assertContains(response, 'A-01-01')
		self.assertContains(response, 'Armazem A')
		self.assertContains(response, 'Pallet')

	def test_locations_page_filters_by_search_plant_storage_and_status(self):
		self.client.login(username='testuser', password='testpassword')

		response = self.client.get(reverse('wharehouses:locations'), {
			'q': 'A-01',
			'plant': self.plant.id,
			'storage': self.storage.id,
			'status': LocationStatus.AVAILABLE,
		})

		locations = response.context['locations_list']
		self.assertEqual(list(locations), [self.location])

	def test_locations_page_filters_blocked_status(self):
		self.client.login(username='testuser', password='testpassword')

		response = self.client.get(reverse('wharehouses:locations'), {
			'status': LocationStatus.BLOCKED,
		})

		self.assertEqual(list(response.context['locations_list']), [self.blocked_location])
