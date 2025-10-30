from .models import SeshatPrivateCommentPart, Polity
from ..accounts.models import Seshat_Expert, TermsVersion

from .terms_utils import user_has_accepted_latest_terms


def terms_banner(request):
    current = TermsVersion.objects.filter(is_active=True).first()
    user = getattr(request, 'user', None)
    show = False
    if current and user and user.is_authenticated and not user_has_accepted_latest_terms(user):
        if request.session.pop('FORCE_TERMS_MODAL', False):  # one-shot
            show = True
    return {'TERMS_SHOW_MODAL': show, 'TERMS_CURRENT': current}

# def terms_banner(request):
#     show = False
#     current = TermsVersion.objects.filter(is_active=True).first()
#     next_url = request.GET.get("next") or "/"
#     user = getattr(request, 'user', None)

#     if current and user and user.is_authenticated:
#         download_like = 'download' in  request.path or 'download' in  next_url
#         if download_like and not user_has_accepted_latest_terms(user):
#             show = True

#     return {'TERMS_SHOW_MODAL': show, 'TERMS_CURRENT': current}


# def terms_banner(request):
#     show = False
#     current = None
#     user = getattr(request, 'user', None)

#     if user and user.is_authenticated:
#         current = TermsVersion.objects.filter(is_active=True).first()
#         if current:
#             # don’t nag on the terms page itself
#             path = getattr(request, 'path', '')
#             #if not path.startswith('/terms/'):
#             show = not user_has_accepted_latest_terms(user)

#     return {
#         'TERMS_SHOW_MODAL': show,
#         'TERMS_CURRENT': current,
#     }


def notifications(request):
    """
    Handle the notifications logic for authenticated users and fetch necessary
    data.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        dict: A dictionary containing:
            - 'notifications_count' (int): The number of private comments for
              the authenticated user.
            - 'all_polities' (QuerySet): A queryset of all polities.
            - 'search_term' (str): The search term submitted in the request,
              if any.
    """
    # Fetch the data you need
    #print("Halooooooooooooooooo")
    if request.user.is_authenticated:
        try:
            my_expert =  Seshat_Expert.objects.get(user_id=request.user.id)
            all_my_private_comments = SeshatPrivateCommentPart.objects.filter(private_comment_reader__id=my_expert.id).exclude(is_done=True)
            notifications_count = len(all_my_private_comments)
        except:
            notifications_count = 0
    else:
        notifications_count = 0

    # Get all polities for the search bar
    all_polities = Polity.objects.all()

    # Get the search term if submitted
    search_term = request.GET.get('search', '')

    # Return the data as a dictionary
    return {
        'notifications_count': notifications_count,
        'all_polities': all_polities,
        'search_term': search_term,
    }
