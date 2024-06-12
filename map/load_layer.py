import os
from django.contrib.gis.utils import LayerMapping
from .models import Railway, Prohibited

railway_mapping = {
    'id': 'id',
    'geom': 'MULTILINESTRING',
}

recomended_mapping = {
    'id': 'id',
    'geom': 'MULTIPOINT',
}


prohibited_mapping = {
    'id': 'id',
    'layer': 'layer',
    'path': 'path',
    'geom': 'MULTIPOLYGON',
}


# rail_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/Railway.shp'))
pro_shp = os.path.abspath(os.path.join(os.path.dirname(__file__), 'data/traylprohibited areas.shp'))

def run(verbose=True):
    # lm = LayerMapping(Railway, rail_shp, railway_mapping, transform=False, encoding='iso-8859-1')
    lm = LayerMapping(Prohibited, pro_shp, prohibited_mapping, transform=False, encoding='iso-8859-1')

    try:
        lm.save(strict=True, verbose=verbose)
    except Exception as e:
        print(f"An error occurred: {e}")

        # If there's an issue, loop through the features to debug
        for feature in lm.layer:
            try:
                lm.save(strict=True, verbose=verbose)
            except Exception as feature_error:
                print(f"Failed to save feature {feature.fid} with geometry {feature.geom}")
                print(f"Error: {feature_error}")
