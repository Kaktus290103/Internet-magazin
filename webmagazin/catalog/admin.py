from django.contrib import admin
from .models import Tovary, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)

class TovaryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'colsklad', 'sale', 'created']
    list_filter = ['price', 'created', 'name']
    list_editable = ['price', 'colsklad', 'sale']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Tovary, TovaryAdmin)
# Register your models here.
