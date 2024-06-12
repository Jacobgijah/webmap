import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, Polygon
from map.models import Prohibited

class Command(BaseCommand):
    help = 'Load GeoJSON data into the database'

    def handle(self, *args, **kwargs):
        with open('/home/jeco/myprojects/django/webmap/webmap/webmap/map/data/prohibited Areas.geojson') as f:
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
            prohibited_area, created = Prohibited.objects.update_or_create(
                pid=props['pid'],
                defaults={
                    'layer': props.get('layer'),
                    'path': props.get('path'),
                    'geom': combined_multipolygon
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created ProhibitedArea {props["pid"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated ProhibitedArea {props["pid"]}'))
