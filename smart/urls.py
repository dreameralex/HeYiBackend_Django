from django.urls import path
from django.contrib import admin


from rest_framework.routers import SimpleRouter
from .views import BannerView,Company_detailView

router = SimpleRouter()
router.register('banner', BannerView, 'banner')
router.register('company_detail', Company_detailView, 'company_detail')

urlpatterns = [

]
urlpatterns+= router.urls