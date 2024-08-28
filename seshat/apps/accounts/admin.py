from django.contrib import admin
from django.contrib.auth.models import User

from .models import Profile, Seshat_Expert, Seshat_Task


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = "Profile"
    fk_name = "user"


class CustomUserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)

    list_display = (
        "username",
        "email",
        "first_name",
        "last_name",
        "is_staff",
        "date_joined",
        "last_login",
        "get_email_confirmed",
    )
    list_select_related = ("profile",)

    def get_location(self, instance):
        return instance.profile.location

    get_location.short_description = "Location"

    def get_email_confirmed(self, instance):
        return instance.profile.email_confirmed

    get_email_confirmed.boolean = True  # Display as a checkbox
    get_email_confirmed.short_description = "Email Confirmed"

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Seshat_Expert)
admin.site.register(Seshat_Task)
