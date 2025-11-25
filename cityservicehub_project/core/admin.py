from django.contrib import admin
from .models import Users,ServiceProvider,Services
# Register your models here.
@admin.register(Users)
class UsersCus(admin.ModelAdmin):
    list_display=('id','name','email','phone','adress')
    search_fields=('name','email','phone')
    list_filter=['name']

@admin.register(ServiceProvider)
class ServiceProviderCus(admin.ModelAdmin):
    list_display=('id','name','email','phone','pincode','address','password')
    search_fields=('name','email','phone','pincode','id')
    list_filter=['name','pincode']


@admin.register(Services)
class ServicesCus(admin.ModelAdmin):
    list_display=('id','service_name')
    search_fields=('service_name','id')
    list_filter=['service_name']
    filter_horizontal=['providers']