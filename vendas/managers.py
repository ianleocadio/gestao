from django.db import models
from django.db.models import Sum, F, FloatField, Max, Avg, Min

class VendaManager(models.Manager):
    def media(self):
        return self.all().aggregate(Avg("valor"))["valor__avg"]

    def media_desconto(self):
        return self.all().aggregate(Avg("desconto"))["desconto__avg"]

    def min(self):
        return self.all().aggregate(Min("valor"))["valor__min"]

    def max(self):
        return self.all().aggregate(Max("valor"))["valor__max"]