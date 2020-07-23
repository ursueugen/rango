from django.contrib import admin

# Customize admin page
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

# Register your models here.
from rango.models import Category, Page
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)