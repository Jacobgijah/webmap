import json
from django.core.management.base import BaseCommand
from django.contrib.gis.geos import GEOSGeometry, MultiLineString, LineString
from map.models import RiverArea

class Command(BaseCommand):
    help = 'Load GeoJSON data into the database'

    def handle(self, *args, **kwargs):
        with open('/home/jeco/myprojects/django/webmap/webmap/webmap/map/data/Rivar.geojson') as f:
            data = json.load(f)
            combined_lines = []
            for feature in data['features']:
                geom = GEOSGeometry(json.dumps(feature['geometry']))
                if isinstance(geom, LineString):
                    combined_lines.append(geom)
                elif isinstance(geom, MultiLineString):
                    combined_lines.extend(geom)
            
            combined_multilinestring = MultiLineString(combined_lines)
            
            # Use the properties of the first feature as the representative properties
            props = data['features'][0]['properties']
            river_area, created = RiverArea.objects.update_or_create(
                id=props['id'],
                defaults={
                    'geom': combined_multilinestring
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created RiverArea {props["id"]}'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Successfully updated RiverArea {props["id"]}'))
