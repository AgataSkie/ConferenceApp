from django.contrib import admin
from .models import Speaker, Session, Track


# Register your models here.
class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')


admin.site.register(Speaker, SpeakerAdmin)


class SessionAdmin(admin.ModelAdmin):
    search_fields = ['title', 'abstract']
    list_filter = ('track__title', 'speaker',)
    list_display = ('title', 'track', 'speaker',)


admin.site.register(Session, SessionAdmin)
admin.site.register(Track)

