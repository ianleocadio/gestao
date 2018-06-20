from django.shortcuts import render
from django.views import View

from .models import Venda
# Create your views here.


class DashboardView(View):
    def get(self, request):

        data = {}
        data["media"] = Venda.objects.media()
        data["media_desc"] =Venda.objects.media_desconto()
        data["min"] = Venda.objects.min()
        data["max"] = Venda.objects.max()

        return render(request, "vendas/dashboard.html", data)