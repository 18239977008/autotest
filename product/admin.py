from django.contrib import admin
from product.models import Product
from apitest.models import Apitest,Apistep,Apis
from apptest.models import Appcase,Appcasestep

# Register your models here.
class ApisAdmin(admin.TabularInline):
    list_display = ['apiname', 'apiurl', 'apiparamvalue', 'apimethod', 'apiresult', 'apistatus', 'creata_time', 'id',
                    'product']
    model = Apis
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'productname', 'productdesc', 'producter', 'create_time']
    inlines = [ApisAdmin]


class AppcaseAdmin(admin.TabularInline):
    list_display = ['appcasename','apptestresult','create_time','id','product']
    model = Appcase
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['productname','productdesc','create_time','id']
    inlines = [AppcaseAdmin]


admin.site.register(Product)  # 把产品模块注册到 Django admin 后台并能显示






