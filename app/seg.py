# -*- coding: utf-8 -*-

import jieba
from collections import Counter
from app.models import weibo,WordCount


STOPWORDS = [u'的',u' ',u'\n',u'他', u'地', u'得', u'而', u'了', u'在', u'是', u'我', u'有', u'和', u'就',  u'不', u'人', u'都', u'一', u'一个', u'上', u'也', u'很', u'到', u'说', u'要', u'去', u'你',  u'会', u'着', u'没有', u'看', u'好', u'自己', u'这']
PUNCTUATIONS = [u'。',u'#', u'，', u'“', u'”', u'…', u'？', u'！', u'、', u'；', u'（', u'）',u'##',u'.',u'@']


cnt = Counter()


def seg(keywords):
    ''' 分词统计 '''
    queryset = weibo.objects.all()
    for obj in queryset:
        data = obj.content
        seg_list = jieba.cut(data)
        for seg in seg_list:
            if seg not in STOPWORDS and seg not in PUNCTUATIONS and seg not in keywords:
                cnt[seg] = cnt[seg] + 1

    result = cnt.most_common(100)
    for ix in result:
        WordCount.objects.create(word=ix[0],count=ix[1])

