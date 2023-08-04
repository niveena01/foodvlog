from django.contrib import admin
from shop.models import catego, products


# Register your models here.
class catadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']


admin.site.register(catego, catadmin)


class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug', 'price', 'stock', 'img', 'available']
    list_editable = ['price', 'stock', 'img', 'available']


admin.site.register(products, prodadmin)
