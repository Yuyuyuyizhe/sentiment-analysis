from aip import AipNlp
from app.models import weibo,AnalyseResult
from decimal import Decimal


# 此处输入baiduAIid
APP_ID = ''
API_KEY = ''
SECRET_KEY = ''


client = AipNlp(APP_ID, API_KEY, SECRET_KEY)



def isPostive(text):
    try:
        score = client.sentimentClassify(text)['items'][0]['positive_prob']
        if score>0.5:
            return score
        else:
            return score
    except:
        return -1



def percent_calc(keyword):
    ''' 计算积极、消极、中立三类情感分别所占百分比 '''
    positive = 0
    neutral = 0
    negative = 0
    queryset = weibo.objects.filter(topic_name=keyword)
    for obj in queryset:
        data = obj.content
        score = isPostive(data)
        if(score > 0.6):
            positive+=1
            result = "positive"
        elif(score > 0 and score < 0.4):
            negative+=1
            result = "negative"
        else:
            neutral+=1
            result = "neutral"
        AnalyseResult.objects.create(score=score,analysis=result,blog_id=obj.id)

    sum = positive+neutral+negative
    percentage = []
    percentage.append(Decimal(positive/sum*100).quantize(Decimal("0.0")))
    percentage.append(Decimal((1-positive/sum-negative/sum)*100).quantize(Decimal("0.0")))
    percentage.append(Decimal(negative/sum*100).quantize(Decimal("0.0")))

    return percentage



def classify_blogs():
    ''' 寻找情感极端的10条微博 '''
    blogs = []
    c=0
    queryset = AnalyseResult.objects.all()
    for obj in queryset:
        if obj.score>=0:
            if obj.score>=0.95 or obj.score<=0.02:
                data = weibo.objects.filter(id=obj.blog_id).first()  # 寻找目标对象
                if obj.score>=0.95:
                    color = "green"
                else:
                    color = "red"
                blog = {'color':color,'username':data.user_name,'blog':data.content,'polarity':obj.analysis}
                blogs.append(blog)
                c+=1
            if c>=10:break # 只展示10条微博内容

    AnalyseResult.objects.all().delete()

    return blogs



def get_all_blogs():
    ''' 获取所有数据 '''
    all_blogs = []
    queryset = AnalyseResult.objects.all()
    for obj in queryset:
        if obj.score>=0:
            data = weibo.objects.filter(id=obj.blog_id).first()  # 寻找目标对象
            blog = {'blog':data.content,'polarity':obj.score}
            all_blogs.append(blog)
    return all_blogs

