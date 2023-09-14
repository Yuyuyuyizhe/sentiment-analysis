from django.shortcuts import render,HttpResponse,redirect
from app import weibo_topic_spyder,analysis,seg
from app.models import weibo,AnalyseResult,UserAdmin
from django import forms
import csv


class UserForm(forms.Form):
    username = forms.CharField(label='账号', max_length=32, widget=forms.TextInput, required=True)
    password = forms.CharField(label='密码', max_length=24, widget=forms.PasswordInput, required=True)

class SearchForm(forms.Form):
	search = forms.CharField(label='在此输入话题或关键词', max_length=500)



def login(request):
    ''' 登录页面 '''

    if request.method == 'GET':
        form = UserForm()
        context = {
            'form':form,
        }
        return render(request, 'login.html', context)

    form = UserForm(request.POST)
    if form.is_valid():
        user_obj = UserAdmin.objects.filter(**form.cleaned_data).first()
        if not user_obj:
            form.add_error("password", "用户名或密码错误")
            return render(request,'login.html', {'form':form})

        request.session["info"] = {'id':user_obj.id,'username':user_obj.username}
        return redirect('/index/')

    return render(request, 'login.html', {'form':form})



def index(request):

    # 检查是否登录
    info = request.session.get("info")
    if not info:
        return redirect('/login/')

    form = SearchForm()
    context = {
        'form': form,
    }
    return render(request, 'index.html', context)



def search(request):
    """ 情感分析页面 """

    if request.method == 'POST':  # 从search框传过来的关键词
        form = SearchForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data['search']
    else:
        form = SearchForm()

    search_list = []
    search_list.append(search)

    weibo_topic_spyder.main(search_list)   # 爬取数据
    seg.seg(search_list)

    global percentage
    percentage = analysis.percent_calc(search)  # 情感分析

    global all_blogs
    all_blogs = analysis.get_all_blogs()

    blogs = analysis.classify_blogs()  # 情感较极端的10条微博

    context = {
        'search':search,
        'percentage':percentage,
        'blogs':blogs,
    }

    return render(request,'search.html',context)



def download_csv(request):
    """ 下载分析数据 """

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="analysis.csv"'

    fieldnames = ['内容', '分数', '情感分析']
    writer = csv.DictWriter(response, fieldnames=fieldnames)
    writer.writeheader()

    for d in all_blogs:
        if d['polarity'] > 0.6:
            word = '积极'
        elif d['polarity'] < 0.4:
            word = '消极'
        else:
            word = '中立'
        writer.writerow({
            '内容': d['blog'],
            '分数': d['polarity'],
            '情感分析': word,
        })

    return response