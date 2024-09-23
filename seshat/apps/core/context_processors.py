from .models import SeshatPrivateCommentPart, Polity
from ..accounts.models import Seshat_Expert


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
    if request.user.is_authenticated:
        try:
            expert = Seshat_Expert.objects.get(user_id=request.user.id)
        except Seshat_Expert.DoesNotExist:
            private_comment_count = 0
        else:
            private_comment_count = SeshatPrivateCommentPart.objects.filter(
                private_comment_reader__id=expert.id
            ).count()
    else:
        private_comment_count = 0

    # Return the data as a dictionary
    return {
        "notifications_count": private_comment_count,
        "all_polities": Polity.objects.all(),
        "search_term": request.GET.get("search", ""),
    }
