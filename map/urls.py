from django.urls import path
from .views import HomePageView, boundary_dataset, prohibited_dataset, railway_dataset, recomended_dataset, river_dataset, warning_dataset, check_coordinate

urlpatterns = [
  path('', HomePageView.as_view(), name='home'),
  path('boundary_data/', boundary_dataset, name='boundary'),
  path('prohibited_data/', prohibited_dataset, name='prohibited'),
  path('railway_data/', railway_dataset, name='railway'),
  path('recomended_data/', recomended_dataset, name='recomended'),
  path('river_data/', river_dataset, name='river'),
  path('warning_data/', warning_dataset, name='warning'),
  path('check_coordinate/', check_coordinate, name='check_coordinate'),
]
