from django.shortcuts import render
from .models import Shop
from .models import JejuOlle

def shop(request):
    shop_list = Shop.objects.all()

    return render(
        request,
        'thirdapp/shop.html',
        {'shop_list': shop_list}
    )

def jeju(request):
    jeju_list = JejuOlle.objects.all()

    return render(
        request,
        'thirdapp/jeju.html',
        {'jeju_list': jeju_list}
    )

def text(request, char):
    return HttpResponse(char)
def date(request, year, month):
    return HttpResponse(
        '%s - %s' % (year, month))