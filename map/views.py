from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
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