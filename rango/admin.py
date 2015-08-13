from django.contrib import admin

# Register your models here.
from rango.models import Category, Page

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class page_admin(admin.ModelAdmin):
    list_display=['title','category','url']
    
admin.site.register(Page,page_admin)