# core/terms_utils.py
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from urllib.parse import quote
from seshat.apps.accounts.models import TermsVersion, TermsAcceptance

def user_has_accepted_latest_terms(user) -> bool:
    if not user.is_authenticated:
        return False
    current = TermsVersion.objects.filter(is_active=True).first()
    if not current:
        return True  # nothing to accept
    return TermsAcceptance.objects.filter(user=user, terms=current).exists()

def require_terms_acceptance(viewfunc):
    def _wrapped(request, *args, **kwargs):
        if not request.user.is_authenticated:
            login_url = f"{reverse('account_login')}?next={quote(request.get_full_path())}"
            return redirect(login_url)
        if not user_has_accepted_latest_terms(request.user):
            #messages.info(request, "Please accept the latest Terms to continue.")
            terms_url = f"{reverse('terms_current')}?next={quote(request.get_full_path())}"
            return redirect(terms_url)
        return viewfunc(request, *args, **kwargs)
    return _wrapped
