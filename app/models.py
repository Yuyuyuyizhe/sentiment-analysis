from django.db import models

# Create your models here.


# 爬取下来的最原始的信息
class weibo(models.Model):
    user_name = models.CharField(max_length=256)
    user_level = models.CharField(max_length=64)
    content = models.TextField()
    zf = models.CharField(max_length=16)
    pl = models.CharField(max_length=16)
    dz = models.CharField(max_length=16)
    start_time = models.CharField(max_length=64)
    keyword = models.CharField(max_length=128)
    topic_name = models.CharField(max_length=128)
    discuss_number = models.CharField(max_length=64)
    read_number = models.CharField(max_length=64)


# 情感计算数据
class AnalyseResult(models.Model):
    score = models.DecimalField(max_digits=4,decimal_places=2)
    analysis = models.CharField(max_length=32)
    blog = models.ForeignKey(to=weibo,to_field="id",on_delete=models.CASCADE)


# 分词统计数据
class WordCount(models.Model):
    word = models.CharField(max_length=64)
    count = models.IntegerField()


# 用户信息数据
class UserAdmin(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=24)
