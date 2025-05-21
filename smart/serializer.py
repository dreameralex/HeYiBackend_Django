from rest_framework import serializers

from .models import Banner, Notice,Company_Detail


# 轮播图表序列化类

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'

# 社区通知序列化类

class NoticeSerializer(serializers.ModelSerializer):

    class Meta:

        model = Notice

        fields = ['id', 'title','igm']

class Conpany_detailSerializer(serializers.ModelSerializer):

    class Meta:

        model = Company_Detail

        fields = '__all__'
