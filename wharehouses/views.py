from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Location, LocationStatus, Plant, Storage


@login_required(login_url='accounts:login_form')
def locations(request):
	locations_list = Location.objects.select_related('storage__plant').order_by('name')

	search = request.GET.get('q', '').strip()
	plant_id = request.GET.get('plant', '')
	storage_id = request.GET.get('storage', '')
	status = request.GET.get('status', '')

	if search:
		locations_list = locations_list.filter(name__icontains=search)
	if plant_id:
		locations_list = locations_list.filter(storage__plant_id=plant_id)
	if storage_id:
		locations_list = locations_list.filter(storage_id=storage_id)
	if status:
		locations_list = locations_list.filter(status=status)

	return render(request, 'locations.html', {
		'locations_list': locations_list,
		'plants': Plant.objects.order_by('name'),
		'storages': Storage.objects.select_related('plant').order_by('name'),
		'location_statuses': LocationStatus.choices,
	})
