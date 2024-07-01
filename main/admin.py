from django.contrib import admin
from . models import Category,Product
# Register your models here.
#admin.site.register(Category)
#admin.site.register(Product)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name','slug')
    prepopulated_field={'slug':('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=('name','price','description')
    list_editable=('price',)
    prepopulated_field={'slug':('name',)}


# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
# list_display = ('name' , 'slug' )
# prepopulated_fields = {'slug' : ('name' ,)}
# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
# list_display =( 'name' , 'category' , 'slug' , 'price' , 'available' )
# list_filter = ( 'category' , 'available' )ist_editable = ( 'price' , 'available' )
# prepopulated_fields = { 'slug' : ( 'name' ,)}
