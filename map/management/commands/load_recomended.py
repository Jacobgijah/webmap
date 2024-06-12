import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, MultiPoint, Point
from map.models import Recomended

class Command(BaseCommand):
    help = 'Load GeoJSON data into the database'

    def handle(self, *args, **kwargs):
        with open('/home/jeco/myprojects/django/webmap/webmap/webmap/map/data/Recomended Zone.geojson') as f:
            data = json.load(f)
            combined_points = []
            for feature in data['features']:
                geom = GEOSGeometry(json.dumps(feature['geometry']))
                if isinstance(geom, Point):
                    combined_points.append(geom)

            combined_multipoint = MultiPoint(combined_points)
            
            # Use a representative id (e.g., the id of the first feature)
            representative_id = data['features'][0]['properties']['id']
            recomended, created = Recomended.objects.update_or_create(
                id=representative_id,
                defaults={
                    'geom': combined_multipoint
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created Recomended {representative_id}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated Recomended {representative_id}'))
