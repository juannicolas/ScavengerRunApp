from django.contrib import admin

from .models import Player, CheckPoint, RecordTime

from .forms import AddTimeForm


class PlayerAdmin(admin.ModelAdmin):
    list_display = ['mprid', 'full_name', 'email', 'phone']


class CheckPointAdmin(admin.ModelAdmin):
    list_display = ["place_name", "id"]


class RecordTimeAdmin(admin.ModelAdmin):
    form = AddTimeForm
    list_display = ('player', 'check_in_time', 'check_point','duration')
    list_filter = ['player']


admin.site.register(Player, PlayerAdmin)
admin.site.register(CheckPoint, CheckPointAdmin)
admin.site.register(RecordTime, RecordTimeAdmin)
