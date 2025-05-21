from django.db import models

# Create your models here.

class Banner(models.Model):

    img = models.ImageField(upload_to='banner', default='banner1.png', verbose_name='图片')

    order = models.IntegerField(verbose_name='顺序')

    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')

    is_delete = models.BooleanField(default=False, verbose_name='是否删除')

    class Meta:
        verbose_name_plural = '轮播图'


class Notice(models.Model):

    title = models.CharField(max_length=64, verbose_name='公共标题')

    content = models.TextField(verbose_name='内容')

    igm = models.ImageField(upload_to='notice', default='notice.png', verbose_name='公告图片')

    create_time = models.DateTimeField(auto_now=True, verbose_name='创建时间')


    class Meta:
        verbose_name_plural = '公告表'

# 首页公司介绍表
class Company_Detail(models.Model):
    img_header = models.ImageField(upload_to='company_datail', default='/banner1.png', verbose_name="标题图片")
    img_detail_header = models.ImageField(upload_to='company_datail', default='/banner1.png', verbose_name="介绍内容标题图片")
    img_detail_detail = models.ImageField(upload_to='company_datail', default='/banner1.png', verbose_name="介绍内容图片")
    name = models.CharField(max_length=32, verbose_name='介绍标题')
    order = models.IntegerField(verbose_name="顺序")
    create_time = models.DateTimeField(auto_now=True, verbose_name="创建时间")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        verbose_name_plural = "介绍表"

    def __str__(self):
        return str(self.img_header)