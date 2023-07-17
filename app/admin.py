from django.contrib import admin

# Register your models here.
from app.models import History


class HistoryAdmin(admin.ModelAdmin):
    
    list_diplay = ['tarixiy', 'zamonaviy']


admin.site.register(History, HistoryAdmin)