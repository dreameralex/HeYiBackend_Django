from django.shortcuts import render

# Create your views here.
from rest_framework.mixins import ListModelMixin

from rest_framework.response import Response

from rest_framework.viewsets import GenericViewSet

from .models import Banner, Notice,Company_Detail

from .serializer import BannerSerializer, NoticeSerializer,Conpany_detailSerializer


class BannerView(GenericViewSet, ListModelMixin):

    queryset = Banner.objects.all().filter(is_delete=False).order_by('order')[:3]

    serializer_class = BannerSerializer

    def list(self, request, *args, **kwargs):

        res = super().list(request, *args, **kwargs)

        notice = Notice.objects.all().order_by('create_time').first()

        serializer = NoticeSerializer(instance=notice)

        return Response({'code': 100, 'msg': '成功', 'banner': res.data, 'notice': serializer.data})



class Company_detailView(GenericViewSet, ListModelMixin):
    queryset = Company_Detail.objects.all().filter(is_delete=False).order_by('order')[:3]

    serializer_class = Conpany_detailSerializer

    def list(self, request, *args, **kwargs):
        res = super().list(request, *args, **kwargs)
        return Response({'code': 100, 'msg': '成功', 'company_detail': res.data})

# 公告接口
from .models import Notice
from  .serializer import NoticeSerializer

class NoticeView(GenericViewSet, ListModelMixin):
    queryset = Notice.objects.all().order_by('create_time')
    serializer_class = NoticeSerializer

# 活动
from .models import Activity
from .serializer import ActivitySerializer
class ActivityView(GenericViewSet,ListModelMixin):
    queryset =Activity.objects.all().order_by('date')
    serializer_class = ActivitySerializer