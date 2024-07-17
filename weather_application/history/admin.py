from django.contrib import admin

from .models import HistoryModel


# Register your models here.
@admin.register(HistoryModel)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ("user", "city", "date")
