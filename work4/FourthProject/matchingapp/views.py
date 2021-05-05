from django.shortcuts import render
import random

def home(request):
    return render(request, 'matchingapp/home.html')

def result(request):
    list=('김서영','박혜준','조원아','이민정','안현주','노은성',
    '김정운','강연우','김소은','문다연','박경나','오예림','이연수',
    '장한빛','황서경','김유진')
    friends=random.sample(list,2)

    return render(request,'matchingapp/result.html',{'friends':friends})
# Create your views here.
