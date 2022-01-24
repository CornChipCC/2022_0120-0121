from django.shortcuts import render
from django.http import HttpResponse
def upload1(request):
    if request.method == 'POST':
        upload_file = request.FILES.get('file') # 파일 객체
        name = upload_file.name # 파일 이름
        size = upload_file.size # 파일 크기
        with open(name, 'wb') as file: # 파일 저장
            for chunk in upload_file.chunks():
                file.write(chunk)
        return HttpResponse('%s<br>%s' % (name, size))
    return render(request, 'file/upload1.html')

def upload2(request):
    if request.method == 'POST':
        upload_files = request.FILES.getlist('file')
        result = ''
        for upload_file in upload_files:
            name = upload_file.name
            size = upload_file.size
            with open(name, 'wb') as file:
                for chunk in upload_file.chunks():
                    file.write(chunk)
            result += '%s<br>%s<hr>' % (name, size)
        return HttpResponse(result)
    return render(request, 'file/upload2.html')    