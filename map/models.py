from django.contrib.gis.db import models


class BoundaryArea(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
      verbose_name_plural = "BoundaryArea"

    def __str__(self):
      return f"BoundaryArea {self.id}"


class Prohibited(models.Model):
    pid = models.IntegerField()
    layer = models.CharField(max_length=254, null=True, blank=True)
    path = models.CharField(max_length=254, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)

    class Meta:
      verbose_name_plural = "Prohibited"

    def __str__(self):
        return f'Prohibited Area {self.id}'


class Railway(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
          verbose_name_plural = "Railway"

    def __str__(self):
      return f"Railway {self.id}"
    

class RiverArea(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiLineStringField(srid=4326)

    class Meta:
          verbose_name_plural = "RiverArea"

    def __str__(self):
      return f"Railway {self.id}"
    

class Recomended(models.Model):
    id = models.BigIntegerField(primary_key=True)
    geom = models.MultiPointField(srid=4326)

    class Meta:
       verbose_name_plural = "Recomended"   

    def __str__(self):
      return f"Recomended {self.id}"


class WarningArea(models.Model):
    id = models.BigIntegerField(primary_key=True)
    layer = models.CharField(max_length=254, null=True, blank=True)
    path = models.CharField(max_length=254, null=True, blank=True)
    geom = models.MultiPolygonField(srid=4326)
   
    def __str__(self):
      return f"WarningArea {self.id}"