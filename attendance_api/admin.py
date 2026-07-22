from django.contrib import admin
from .models import Attendance


@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "date")
    search_fields = ("user__username",)
    list_filter = ("date",)