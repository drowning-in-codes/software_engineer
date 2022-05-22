from django.db import models


# Create your models here.

class userinfo(models.Model):

    account = models.CharField(max_length=32,verbose_name='用户账号', unique=True)
    password = models.CharField(max_length=64, verbose_name='密码')
    name = models.CharField(max_length=32, verbose_name='网名')
    def __str__(self):
        return self.account

class questioninfo(models.Model):

    number = models.CharField(max_length=7, verbose_name='题目编号', unique=True)
    topic = models.CharField(max_length=1000, verbose_name='题目',unique=True)
    A_Key = models.CharField(max_length=1000, verbose_name='答案A')
    B_Key = models.CharField(max_length=1000, verbose_name='答案B')
    C_Key = models.CharField(max_length=1000, verbose_name='答案C')
    D_Key = models.CharField(max_length=1000, verbose_name='答案D')
    # R_Key = models.CharField(max_length=1, verbose_name='正确答案')
    R_Key = models.CharField(max_length=1, choices=(('A', '答案A'), ('B', '答案B'), ('C', '答案C'), ('D', '答案D')), verbose_name='正确答案', blank=True, null=True)

    def __str__(self):
        return self.number

class record(models.Model):
    user = models.ForeignKey(to='userinfo', on_delete=models.CASCADE)
    question = models.ForeignKey(to='questioninso',  on_delete=models.CASCADE)
    evaluate = models.CharField(max_length=1, choices=(('T', '正确'), ('F', '错误')), verbose_name='正误')
    key = models.CharField(max_length=1, choices=(('A', '答案A'), ('B', '答案B'), ('C', '答案C'), ('D', '答案D')), verbose_name='已选答案', blank=True, null=True)


