from django.contrib import admin
from rango.models import Category,CategoryAdmin, Page, PageAdmin
from django.contrib.auth.models import User
from rango.models import UserProfile


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)