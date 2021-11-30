from __future__ import unicode_literals

from django.contrib import admin

from app.models import Price

class PriceAdmin(admin.ModelAdmin):
    list_display = ['id', 'date', 'open_price', 'close_price']


admin.site.register(Price, PriceAdmin)