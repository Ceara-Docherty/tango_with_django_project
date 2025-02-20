from django.contrib import admin
from rango.models import Category, Page

# Register your models here.

class PageAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'url')

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category)
admin.site.register(Page)