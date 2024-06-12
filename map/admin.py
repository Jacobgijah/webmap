from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin
from .models import Railway, Prohibited, Recomended, BoundaryArea, RiverArea, WarningArea


@admin.register(BoundaryArea)
class BoundaryAreaAdmin(LeafletGeoAdmin):
  list_display = ['geom']


@admin.register(Prohibited)
class ProhibitedAdmin(LeafletGeoAdmin):
  list_display = ['layer', 'geom']


@admin.register(Railway)
class RailwayAdmin(LeafletGeoAdmin):
  list_display = ['geom']


@admin.register(RiverArea)
class RiverAreaAdmin(LeafletGeoAdmin):
  list_display = ['geom']


@admin.register(Recomended)
class RecomendedAdmin(LeafletGeoAdmin):
  list_display = ['geom']


@admin.register(WarningArea)
class WarningAreaAdmin(LeafletGeoAdmin):
  list_display = ['layer', 'geom']


