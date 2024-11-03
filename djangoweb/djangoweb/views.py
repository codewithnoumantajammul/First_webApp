from django.http import HttpResponse
from django.shortcuts import render
import operator
from . import counter

def home(request):
    return render(request,'index.html')

def downloads(request):
    return HttpResponse('<h1>No downloads</h1>')

def result(request):
    article = request.GET['article']
    var_dict,word_count = counter.count(article)
    return render(request,'result.html',{'article':article,'word_count':word_count,'dict_words':var_dict})