from django.shortcuts import render
from django.http import JsonResponse
from app.models import WordCount
from app.analysis import isPostive


def chart_bar(request):
    ''' 绘制词频统计条形图 '''

    queryset = WordCount.objects.all()
    word = []
    count = []
    c = 0
    for obj in queryset:
        word.append(obj.word)
        count.append(obj.count)
        c+=1
        if c>=10:break

    result = {
        'status':True,
        'data':{
            'count':count,
            'word':word,
        }
    }

    # print(result)
    WordCount.objects.all().delete()

    return JsonResponse(result)