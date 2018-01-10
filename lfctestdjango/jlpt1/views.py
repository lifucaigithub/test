#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from forms import ExamInfoForm

# Create your views here.
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
def exam(request):
    if request.method == 'POST':
        form = ExamInfoForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lev = request.POST.getlist('level')[0]
            sex = request.POST.getlist('sex')[0]
            return HttpResponse('Thank you,姓名 is: %s,难度 is : %s,性别 is:%s'%(name,lev,sex))
    else:
        form = ExamInfoForm()
    return render(request, 'index.html', {'form': form})



