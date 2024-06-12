import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry
from map.models import BoundaryArea

class Command(BaseCommand):
    help = 'Load GeoJSON data into the database'

    def handle(self, *args, **kwargs):
        with open('/home/jeco/myprojects/django/webmap/webmap/webmap/map/data/Boundary.geojson') as f:
            data = json.load(f)
            for feature in data['features']:
                geom = GEOSGeometry(json.dumps(feature['geometry']))
                props = feature['properties']
                boundary_area, created = BoundaryArea.objects.update_or_create(
                    id=props['id'],
                    defaults={
                        'geom': geom
                    }
                )
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Successfully created Boundary area {props["id"]}'))
                else:
                    self.stdout.write(self.style.SUCCESS(f'Successfully updated Boundary area {props["id"]}'))
