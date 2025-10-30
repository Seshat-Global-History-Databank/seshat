from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .forms import SeshatExpertAdminForm

from .models import Profile, Seshat_Expert, Seshat_Task, TermsVersion, TermsAcceptance

from django.contrib.auth import get_user_model

User = get_user_model()
######EMAIL_CONFIRMATION_BRANCH is the keyword that needs to be searched


class TermsAcceptanceInline(admin.TabularInline):
    model = TermsAcceptance
    extra = 0
    can_delete = False
    readonly_fields = ("user", "full_name", "accepted_at", "ip_address", "user_agent")
    fields = ("user", "full_name", "accepted_at", "ip_address", "user_agent")
    show_change_link = True  # link to the Acceptance object

    def has_add_permission(self, request, obj=None):
        # You shouldn't be manually adding "yes they accepted" entries
        return False
    
    def full_name(self, obj):
        """
        Show "First Last" nicely.
        Falls back to username if names are blank.
        """
        if not obj or not obj.user_id:
            return "-"

        first = getattr(obj.user, "first_name", "") or ""
        last = getattr(obj.user, "last_name", "") or ""
        full = (first + " " + last).strip()

        return full if full else " - "
    
@admin.register(TermsVersion)
class TermsVersionAdmin(admin.ModelAdmin):
    list_display = (
        "published_at",
        "is_active",
        "short_preview",
        "acceptance_count",
    )
    list_filter = ("is_active", "published_at")
    search_fields = ("body_html",)
    ordering = ("-published_at",)

    readonly_fields = ("published_at", "preview_html")

    inlines = [TermsAcceptanceInline]

    fieldsets = (
        ("Metadata", {
            "fields": (
                "is_active",
                "published_at",
            )
        }),
        ("Agreement Text", {
            "description": "This is the exact text users saw / agreed to. Do not edit retroactively unless you're creating a new version.",
            "fields": (
                "body_html",
                "preview_html",
            )
        }),
    )

    def short_preview(self, obj):
        """
        Short plain-text-ish preview for list_display.
        We'll strip HTML tags very lightly so the table doesn't explode.
        """
        # crude strip of tags for preview:
        import re
        text_only = re.sub("<[^<]+?>", "", obj.body_html or "")
        preview = (text_only[:60] + "…") if len(text_only) > 60 else text_only
        return preview
    short_preview.short_description = "Preview"

    def preview_html(self, obj):
        """
        Read-only pretty block in the detail page to visually inspect
        what the user agreement looks like.
        """
        if not obj.body_html:
            return "-"
        return format_html(
            '<div style="max-height:200px; overflow:auto; border:1px solid #ccc; padding:0.5rem; background:#fafafa; font-size:0.8rem; line-height:1.4;">{}</div>',
            mark_safe(obj.body_html),
        )
    preview_html.short_description = "Rendered terms (preview)"

    def acceptance_count(self, obj):
        return obj.termsacceptance_set.count()
    acceptance_count.short_description = "# Accepted"

@admin.register(TermsAcceptance)
class TermsAcceptanceAdmin(admin.ModelAdmin):
    list_display = (
        "user_display",
        "full_name",
        "accepted_at",
        "ip_address",
        "short_user_agent",
    )
    list_filter = ("accepted_at",)
    search_fields = (
        "user__username",
        "user__email",
        "full_name",
        "ip_address",
        "user_agent",
    )
    ordering = ("-accepted_at",)

    readonly_fields = (
        "user",
        "full_name",
        "accepted_at",
        "ip_address",
        "user_agent",
    )

    fieldsets = (
        ("Acceptance Info", {
            "fields": (
                "user",
                "accepted_at",
            )
        }),
        ("Client Details", {
            "fields": (
                "ip_address",
                "user_agent",
            )
        }),
    )


    def full_name(self, obj):
        """
        Show "First Last" nicely.
        Falls back to username if names are blank.
        """
        if not obj or not obj.user_id:
            return "-"

        first = getattr(obj.user, "first_name", "") or ""
        last = getattr(obj.user, "last_name", "") or ""
        full = (first + " " + last).strip()

        return full if full else " - "


    def user_display(self, obj):
        # nice display for the user in list_display
        if hasattr(obj.user, "email") and obj.user.email:
            return f"{obj.user.email}"
        return obj.user.username
    user_display.short_description = "User"

    def short_user_agent(self, obj):
        if not obj.user_agent:
            return ""
        # show just the first ~40 chars
        ua = obj.user_agent
        return ua[:40] + ("…" if len(ua) > 40 else "")
    short_user_agent.short_description = "User Agent"




class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'


class CustomUserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline, )

    list_display = ('username', 'email', 'first_name',
                    'last_name', 'is_staff', 'date_joined', 'last_login','get_email_confirmed')
    list_select_related = ('profile', )

    def get_location(self, instance):
        return instance.profile.location
    get_location.short_description = 'Location'

    def get_email_confirmed(self, instance):
        return instance.profile.email_confirmed
    get_email_confirmed.boolean = True  # Display as a checkbox
    get_email_confirmed.short_description = 'Email Confirmed'

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
#admin.site.unregister(Seshat_Expert)
admin.site.register(Seshat_Task)
#admin.site.register(TermsVersion)
#admin.site.register(TermsAcceptance)



class SeshatExpertAdmin(admin.ModelAdmin):
    """
    Custom admin for Seshat_Expert model.
    """
    form = SeshatExpertAdminForm

    list_display = ('id', 'get_full_name', 'role', 'get_username', 'email', 'is_staff', 'is_active', 'last_login', 'date_joined')
    list_filter = ('role',)  # Add filters for roles
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'user__email')  # Enable search by user details

    ordering = ('user__last_name', 'user__first_name')  # Order by name

    @admin.display(description='Full Name')
    def get_full_name(self, obj):
        """
        Returns the full name of the user.
        """
        if obj.user.first_name and obj.user.last_name:
            return f"{obj.user.first_name} {obj.user.last_name}"
        return "N/A"

    @admin.display(description='Username')
    def get_username(self, obj):
        """
        Returns the username of the user.
        """
        return obj.user.username
    
    @admin.display(description='Last login')
    def last_login(self, obj):
        return obj.user.last_login
    
    @admin.display(description='Joined')
    def date_joined(self, obj):
        return obj.user.date_joined

    @admin.display(description='Email')
    def email(self, obj):
        """
        Returns the email of the user.
        """
        return obj.user.email
    
    @admin.display(description='Active')
    def is_active(self, obj):
        return obj.user.is_active

    @admin.display(description='Staff')
    def is_staff(self, obj):
        return obj.user.is_staff

    

admin.site.register(Seshat_Expert, SeshatExpertAdmin)


