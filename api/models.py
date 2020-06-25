from django.db import models
import uuid
# Create your models here.


class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=120, unique=True, verbose_name='Name')
    direction = models.CharField(max_length=120, verbose_name="Direction")
    phone = models.IntegerField()

    def __str__(self):
        return self.name


class Recipe(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")
    type = models.CharField(max_length=20, choices=[('BREAKFAST', 'Breakfast'),('LUNCH', 'Lunch'),('COFFEE','coffee'),('DINNER', 'Dinner')])
    thumbnail = models.ImageField(upload_to='recipe_thumbnails', default="recipe_thumbnails/default.png")


    def __str__(self):
        return self.name

class Ingredients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length=120, unique=True, verbose_name="Name")

    def __str__(self):
        return self.name
