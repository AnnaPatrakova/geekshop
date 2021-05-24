from django.contrib import admin

# Register your models here.
from mainapp.models import ProductCategory, Product


admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')
    fields = ('name', 'image', 'description', ('price', 'quantity'), 'category')
    readonly_fields = ('description',)
    ordering = ('price',)
    search_fields = ('name',)