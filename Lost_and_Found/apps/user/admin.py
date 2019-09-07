from django.contrib import admin
from .models import *

class UserAdmin(admin.ModelAdmin):
    list_display = ['id','first_name','username','date_joined']
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_filter = ['first_name','username']
    search_fields = ['first_name','username']
admin.site.register(User,UserAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['id','item_email','status','time','area','location','create_time','detail','price']
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_filter = ['location','detail','status','area']
    search_fields = ['detail','location','area']
admin.site.register(Item,ItemAdmin)

class SuggestionAdmin(admin.ModelAdmin):
    list_display = ['id','content','create_time']
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_filter = ['create_time']
    search_fields = ['content']
admin.site.register(Suggestion,SuggestionAdmin)

class PictureAdmin(admin.ModelAdmin):
    list_display = ['id','pic1','pic2','pic3']
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_filter = ['item_id']
    search_fields = ['item_id']
admin.site.register(Picture,PictureAdmin)

class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_per_page = 5
    actions_on_top = True
    actions_on_bottom = True
    list_filter = ['name']
    search_fields = ['name']
admin.site.register(Type,TypeAdmin)
