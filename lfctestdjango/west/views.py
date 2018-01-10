#from django.core.context_processors import csrf
from west.models import Character
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.views.decorators import csrf
# Create your views here.
import sys

default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

def staff(request):
    staff_list = Character.objects.all()
    #staff_str  = map(str, staff_list)
    #context   = {'label': ' '.join(staff_str)}
    return render(request, 'templay.html', {'staffs':staff_list})

def templay(request):
    context = {}
    context['label'] = 'Hello World!'
    return render(request, 'templay.html', context)

def formGet(request):
    return render(request, 'getform.html')

def formPost(request):
    return render(request, 'postform.html')

def investigateGet(request):
    rlt = request.GET['staff']
    return HttpResponse(rlt)

def investigatePost(request):
    if request.method =='POST':
        submitted  = request.POST['staff']
        new_record = Character(name = submitted)
        new_record.save()
    staff_list = Character.objects.all()
    return render(request, 'postform.html', {'staffs':staff_list})