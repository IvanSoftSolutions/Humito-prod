from django.db import models


class VapeInfo(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField()
    price = models.FloatField(default=0.0)
    multiplier = models.FloatField(default=0.0)
    flavors = models.JSONField()
    url = models.URLField()
    available = models.BooleanField()
    
    def __str__(self):
        return self.name
    
    @property
    def item_price_calc(self):
        return 5 * round(round(self.price * self.multiplier) / 5)