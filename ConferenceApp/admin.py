from django.contrib import admin
from .models import Speaker, Session, Track


class SpeakerAdmin(admin.ModelAdmin):

    list_display = ('name', 'bio')
    fieldsets = (
        ("General Information", {"fields": ("name", "bio",)
        }),
        ("Social media", {
            "classes": ("collapse",),
            "fields": ("fb", "twitter",)
        })
    )


admin.site.register(Speaker, SpeakerAdmin)


class SessionAdmin(admin.ModelAdmin):

    def status_approved(self, request, queryset):
        rows_updated = queryset.update(status='a')
        success_message = '{} session(s) updated'.format(rows_updated)
        self.message_user(request, success_message)

    status_approved.short_description = "Mark as approved"

    def status_rejected(self, request, queryset):
        rows_updated = queryset.update(status='r')
        success_message = '{} session(s) updated'.format(rows_updated)
        self.message_user(request, success_message)

    status_rejected.short_description = "Mark as rejected"

    search_fields = ['title', 'abstract']
    list_filter = ('track__title', 'speaker', 'status')
    list_display = ('title', 'speaker', 'status')
    actions = [status_approved, status_rejected]




admin.site.register(Session, SessionAdmin)
admin.site.register(Track)

