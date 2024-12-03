# middleware.py
from django.contrib.auth import get_user_model, login
from django.conf import settings

class AutoLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            User = get_user_model()
            user, created = User.objects.get_or_create(username='testuser', defaults={'password':'testpass', 'is_staff':True, 'is_superuser':True})
            if created:
                user.set_password(user.password)
                user.save()
            # Specify the authentication backend
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            login(request, user)
        response = self.get_response(request)
        return response