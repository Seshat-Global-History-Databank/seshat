# middleware.py
from django.contrib.auth import get_user_model, login
from django.conf import settings
from django.shortcuts import redirect
from django.urls import reverse, resolve, Resolver404

from .terms_utils import user_has_accepted_latest_terms

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
    



###################################

# core/middleware.py

EXEMPT_PREFIXES = ('/admin/', '/static/', '/media/')
EXEMPT_VIEWNAMES = {
    'terms_current',
    'terms_accept',
    'account_login',
    'account_logout',
}

class EnforceLatestTermsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path or ''

        # Skip obvious prefixes
        if any(path.startswith(p) for p in EXEMPT_PREFIXES):
            return self.get_response(request)

        user = getattr(request, 'user', None)
        if not (user and user.is_authenticated):
            return self.get_response(request)

        # Acceptance is recorded per TermsVersion, so accepting an older version
        # does not satisfy the currently active agreement.
        if user_has_accepted_latest_terms(user):
            request.session.pop('FORCE_TERMS_MODAL', None)
            request.session.pop('TERMS_MODAL_SHOWN', None)
            return self.get_response(request)

        # Respect explicit exempt views
        try:
            view_name = resolve(request.path_info).view_name
        except Resolver404:
            view_name = None
        if view_name in EXEMPT_VIEWNAMES:
            return self.get_response(request)

        # The original workflow shows the active agreement in a modal on the
        # requested page. The context processor consumes this one-shot flag.
        request.session['FORCE_TERMS_MODAL'] = True

        # Downloads cannot render the modal, so return to the homepage where it
        # will be shown before the user can retry the download.
        if 'download' in path:
            return redirect(reverse('seshat-index'))

        return self.get_response(request)


#############################

# EXEMPT_PREFIXES = ('/admin/', '/api/', '/static/', '/media/')

# EXEMPT_VIEWNAMES = {"terms_current", "terms_accept", "account_login", "logout", "seshat-index"}


# # class EnforceLatestTermsMiddleware:
# #     def __init__(self, get_response): self.get_response = get_response

# #     def __call__(self, request):
# #         # skip obvious prefixes
# #         if any(request.path.startswith(p) for p in EXEMPT_PREFIXES):
# #             return self.get_response(request)

# #         # need authenticated user
# #         user = getattr(request, 'user', None)
# #         if not (user and user.is_authenticated):
# #             return self.get_response(request)

# #         # has user accepted latest?
# #         if user_has_accepted_latest_terms(user):
# #             return self.get_response(request)

# #         # resolve view name to honor exemptions
# #         try:
# #             view_name = resolve(request.path_info).view_name
# #         except Resolver404:
# #             view_name = None

# #         if view_name in EXEMPT_VIEWNAMES:
# #             return self.get_response(request)

# #         print("Also here.....")
# #         terms_url = f"{reverse('terms_current')}?next={request.get_full_path()}"
# #         return redirect(terms_url)


# class EnforceLatestTermsMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         # skip obvious prefixes
#         if any(request.path.startswith(p) for p in EXEMPT_PREFIXES):
#             return self.get_response(request)

#         user = getattr(request, 'user', None)
#         if not (user and user.is_authenticated):
#             return self.get_response(request)

#         # already accepted → continue
#         if user_has_accepted_latest_terms(user):
#             return self.get_response(request)

#         # honor explicit exempt views
#         try:
#             view_name = resolve(request.path_info).view_name
#         except Resolver404:
#             view_name = None
#         if view_name in EXEMPT_VIEWNAMES:
#             return self.get_response(request)

#         # 🔑 Instead of redirecting, set a one-shot session flag for the modal
#         # If you want it ONLY on download pages, gate with DOWNLOAD_PATTERN here:
#         if 'download' in request.path:
#             #print("Hayyyyyyyyyyyyyy....")
#             request.session['FORCE_TERMS_MODAL'] = True

#         # Let the original view render; the modal will show from the base template
#         return self.get_response(request)
