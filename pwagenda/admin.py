from django.contrib import admin
from pwagenda.models import Meeting
from pwagenda.models import UserProfile

class MeetingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Meeting, MeetingAdmin)
admin.site.register(UserProfile)
