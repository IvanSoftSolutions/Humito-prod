from django.db import models


class VapeInfo(models.Model):
    name = models.CharField(max_length=200)
    hits = models.CharField(max_length=32)
    price = models.IntegerField(default=0)
    multiplier = models.FloatField(default=0.0)
    flavors = models.JSONField(default=None, blank=True, null=True)
    available = models.BooleanField()
    image = models.CharField(default='')
    
    def __str__(self):
        return self.name
    
    @property
    def item_price_calc(self):
        return 5 * round(round(self.price * self.multiplier) / 5)
    
class VapeImages(models.Model):
    image = models.ImageField()
    vape_id = models.ForeignKey(VapeInfo, on_delete=models.CASCADE)
    