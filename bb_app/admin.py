from django.contrib import admin
from .models import Campus,Events,EventImages,EventRegistrations,Message,EventRegistrationsHackathon

class EventImagesInline(admin.TabularInline):
    model = EventImages
    extra = 3

class EventImagesAdmin(admin.ModelAdmin):
    inlines = [ EventImagesInline, ]

admin.site.register(Campus)
admin.site.register(Events, EventImagesAdmin)
admin.site.register(EventRegistrations)
admin.site.register(EventRegistrationsHackathon)
admin.site.register(Message)
# Register your models here.