from django.contrib import admin
from lists.models import Item, List # Import Model ของเราเข้ามา

admin.site.register(Item) # ลงทะเบียนตาราง Item
admin.site.register(List) # ลงทะเบียนตาราง List