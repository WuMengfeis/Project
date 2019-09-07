from django.contrib import admin
from .models import *

# admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','name','author','price']
    list_per_page = 3
    actions_on_top = True
    actions_on_bottom = True
    list_filter = ['name']
    search_fields = ['name']
    # date_hierarchy = 'pub_date'

admin.site.register(Book,BookAdmin)

