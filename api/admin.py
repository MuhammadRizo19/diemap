from django.contrib import admin
from .models import DieMap

@admin.register(DieMap)
class DieMapAdmin(admin.ModelAdmin):
    list_display = ('sapcode', 'benkam', 'synced_at')
    search_fields = ('sapcode', 'benkam')
    readonly_fields = ('synced_at',)
