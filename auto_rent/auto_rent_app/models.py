from django.db import models


class Cars(models.Model):

    year = models.IntegerField("Year of release", default=1900)
    mileage = models.IntegerField("Vehicle mileage", default=0)
    model = models.CharField("Model", max_length=200)
    color = models.CharField("Color", max_length=200)
    TRANSMISSION_TYPES = (("Auto", "Автоматичекая"),
                          ("CVT", "Роботизированная"),
                          ("Manual", "Механическая"))
    transmission = models.CharField("Transmission", choices=TRANSMISSION_TYPES, max_length=200)
    body_style = models.CharField("Body style", max_length=200)
    price = models.DecimalField("Price", max_digits=9, decimal_places=2)
    time_create = models.DateTimeField('Created date', auto_now_add=True)
    brand_id = models.ForeignKey('CarBrands', on_delete=models.CASCADE, null=True, related_name='brand')

    def __str__(self):
        return self.model


class CarBrands(models.Model):
    label = models.CharField("Brand's name", max_length=50)

    def __str__(self):
        return self.label
