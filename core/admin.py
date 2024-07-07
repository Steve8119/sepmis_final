from django.contrib import admin
from .models import Profile, Unit, Notification, ChatMessage

class UnitInline(admin.TabularInline):
    model = Unit
    extra = 1

class NotificationInline(admin.TabularInline):
    model = Notification
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'admission_number', 'course', 'year_of_studies', 'total_fees', 'fees_balance')
    search_fields = ('user__username', 'full_name', 'admission_number', 'course')
    inlines = [UnitInline, NotificationInline]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Unit)
admin.site.register(Notification)
admin.site.register(ChatMessage)
