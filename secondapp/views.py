from django.shortcuts import render
from django.http import HttpResponse
from .models import Course
from .models import ArmyShop

def main(request):
    return HttpResponse('<u>Main</u>')
# Create your views here.
def insert(request):
    # 1-linux 입력
    Course.objects.create(name='데이터 분석', cnt = 30)
    # 2-python 입력
    c = Course(name='데이터 수집', cnt = 20)
    c.save()
    # 3-html/css/js 입력
    Course(name='웹개발', cnt = 25).save()
    # 4-django 입력
    Course(name='인공지능', cnt = 25).save()
    return HttpResponse('데이터 입력 완료')

def show(request):
    # course = Course.objects.all()
    # result = ''
    # for c in course:
    #     result += c.name + '\t'  + str(c.cnt) + '<br>'
    # return HttpResponse(result)
    course = Course.objects.all()
    return render(
        request,
        'secondapp/show.html', 
        {'data': course})

def army(request):
    # prd = request.GET.get('prd', '')
    prd = request.GET.get('prd', '')
    try :
        shop = ArmyShop.objects.filter(name__contains = prd)
    except : 
        shop = ArmyShop.objects.all()
    return render(
        request,
        'secondapp/army_shop.html', 
        {'shop': shop})

def army_shop2(request,year,month):
    shop = ArmyShop.objects.filter(year=year, month=month)

    result = ''
    for i in shop:
        result += '%s %s %s<br>' % (i.year, i.month, i.name)
    return HttpResponse()

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.forms.models import model_to_dict
@csrf_exempt
def ajaxGet(request):
    #QeurySet []
    c = Course.objects.all()

    data = []
    # model_to_dict - 조회된 데이터를 dict 형태로 변경
    for a in c:
        d = model_to_dict(a)
        data.append(d)
    return JsonResponse(data, safe=False)

def ajaxExam(request):
    return render( request, 
                    'secondapp/ajax_exam.html')
from django.shortcuts import redirect
from .forms import CourseForm
def course_create(request):
    ## form 미 사용시 작성되는 코드
    # name = request.POST.get('name')
    # cnt = request.POST.get('cnt')
    # c = Course(name=name, cnt=cnt)
    # c.save()

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            form.save()
            return redirect('firstapp:post')
    else:
        form = CourseForm()

    return render(request, 'secondapp/course_create.html', { 'form': form })