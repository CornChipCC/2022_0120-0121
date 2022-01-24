from django.shortcuts import render
from secondapp.models import ArmyShop
from django.core.paginator import Paginator

def army_shop(request):
    datas = ArmyShop.objects.order_by('-id')
    p = Paginator(datas, 10)
    info = p.page(1)
    context = {
        'info' : info
    }
    return render(request, 'paging/army_shop.html', context)