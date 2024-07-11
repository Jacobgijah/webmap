from django.core.serializers import serialize
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .models import Prohibited, Railway, BoundaryArea, Recomended, RiverArea, WarningArea

class HomePageView(TemplateView):
  template_name = 'index.html'


def boundary_dataset(request):
  boundary = serialize('geojson', BoundaryArea.objects.all())
  return HttpResponse(boundary, content_type='application/json')


def prohibited_dataset(request):
  prohibited = serialize('geojson', Prohibited.objects.all())
  return HttpResponse(prohibited, content_type='application/json')

def railway_dataset(request):
  railway = serialize('geojson', Railway.objects.all())
  return HttpResponse(railway, content_type='application/json')


def recomended_dataset(request):
  recomended = serialize('geojson', Recomended.objects.all())
  return HttpResponse(recomended, content_type='application/json')


def river_dataset(request):
  river = serialize('geojson', RiverArea.objects.all())
  return HttpResponse(river, content_type='application/json')


def warning_dataset(request):
  warning = serialize('geojson', WarningArea.objects.all())
  return HttpResponse(warning, content_type='application/json')

def check_coordinate(request):
    latitude = request.GET.get('latitude')
    longitude = request.GET.get('longitude')
    point = Point(float(longitude), float(latitude), srid=4326)
    
    # Check if the point is within any boundary area
    if not BoundaryArea.objects.filter(geom__contains=point).exists():
        return JsonResponse({'status': 'error', 'message': 'Area out of boundary'})

    # Check in prohibited areas
    prohibited = Prohibited.objects.filter(geom__contains=point).first()
    if prohibited:
        return JsonResponse({'status': 'success', 'area': 'Prohibited Area', 'label': str(prohibited)})

    # Check in railway areas
    railway = Railway.objects.filter(geom__contains=point).first()
    if railway:
        return JsonResponse({'status': 'success', 'area': 'Railway', 'label': str(railway)})

    # Check in recommended areas
    recommended = Recomended.objects.filter(geom__contains=point).first()
    if recommended:
        return JsonResponse({'status': 'success', 'area': 'Recommended', 'label': str(recommended)})

    # Check in river areas
    river = RiverArea.objects.filter(geom__contains=point).first()
    if river:
        return JsonResponse({'status': 'success', 'area': 'River', 'label': str(river)})

    # Check in warning areas
    warning = WarningArea.objects.filter(geom__contains=point).first()
    if warning:
        return JsonResponse({'status': 'success', 'area': 'Warning Area', 'label': str(warning)})

    return JsonResponse({'status': 'error', 'message': 'Area not found in any category'})
