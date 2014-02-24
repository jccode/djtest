
from django.contrib import admin
from models import Food, MPTTFood
from mptt.admin import MPTTModelAdmin


admin.site.register(Food)
admin.site.register(MPTTFood, MPTTModelAdmin)
