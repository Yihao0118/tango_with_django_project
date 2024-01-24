from django.contrib import admin
from rango.models import Category,CategoryAdmin, Page, PageAdmin

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)