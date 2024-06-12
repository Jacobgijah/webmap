import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Polygon
from map.models import WarningArea

class Command(BaseCommand):
    help = 'Load GeoJSON data into the database'

    def handle(self, *args, **kwargs):
        with open('/home/jeco/myprojects/django/webmap/webmap/webmap/map/data/Warning Area.geojson') as f:
            data = json.load(f)
            combined_polygons = []
            for feature in data['features']:
                geom = GEOSGeometry(json.dumps(feature['geometry']))
                if isinstance(geom, Polygon):
                    combined_polygons.append(geom)
                elif isinstance(geom, MultiPolygon):
                    combined_polygons.extend(geom)

            combined_multipolygon = MultiPolygon(combined_polygons)
            
            # Use the properties of the first feature as the representative properties
            props = data['features'][0]['properties']
            warning_area, created = WarningArea.objects.update_or_create(
                id=props['id'],
                defaults={
                    'layer': props.get('layer'),
                    'path': props.get('path'),
                    'geom': combined_multipolygon
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created WarningArea {props["id"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated WarningArea {props["id"]}'))
