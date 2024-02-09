from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Retrieving stirng response by using Function Based View
def fbv_string(request):
    return HttpResponse('<h1>This is the string from fbv_string')


# Retrieving string response by using Class Based View
class CbvString(View):
    def get(self,request):
        return HttpResponse('<h1>This is the string from CbvString')

# Rendering html page by using Function Based View

def fbv_html(request):
    return render(request,'fbv_html.html')

# Renderirng html page by using Class Based View

class CbvHtml(View):
    def get(self,request):
        return render(request,'CbvHtml.html')

# Inserting form data by using Function Based View
def insert_student_by_fbv(request):
    SFO=StudentForm()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('insert_student_by_fbv id done...')
    return render(request,'insert_student_by_fbv.html',d)


# Inserting form data by using Class Based View

class Insert_student_by_Cbv(View):
    def get(self,request):
        ESFO=StudentForm()
        d={'ESFO':ESFO}
        return render(request,'Insert_student_by_Cbv.html',d)

    def post(self,request):
        SFDO=StudentForm(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('Insert_student_by_Cbv is done...')


class Cbv_Template(TemplateView):
    template_name='Cbv_Template.html'