from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Profile, Seshat_Expert, Seshat_Task
######EMAIL_CONFIRMATION_BRANCH is the keyword that needs to be searched


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


class SeshatExpertAdmin(admin.ModelAdmin):
    """
    Custom admin for Seshat_Expert model.
    """
    list_display = ('id', 'get_full_name', 'role', 'get_username', 'email', 'is_staff', 'is_active', 'last_login', 'date_joined')
    list_filter = ('role',)  # Add filters for roles
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




