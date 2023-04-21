from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
from app.models import *
# Create your views here.
def insert_topic(request):
    To=TopicForm()
    d={'To':To}
    if request.method=='POST':
        form_data=TopicForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Topic inserted successfully')
    return render(request,'insert_topic.html',d)




def insert_webpage(request):
    Wo=WebpageForm()
    d={'Wo':Wo}
    if request.method=='POST':
        form_data=WebpageForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            return HttpResponse('Webpage inserted successfully')
    return render(request,'insert_webpage.html',d)

def display_webpage(request):
    WO=Webpage.objects.all()
    d1={'WO':WO}
    return render(request,'display_webpage.html',d1)