from django.contrib import admin

# Register your models here.
from .models import Banner, Notice,Company_Detail,Activity

admin.site.register(Banner)
admin.site.register(Notice)
admin.site.register(Company_Detail)
admin.site.register(Activity)