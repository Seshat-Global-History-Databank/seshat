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
            my_expert = Seshat_Expert.objects.get(user_id=request.user.id)
            all_my_private_comments = SeshatPrivateCommentPart.objects.filter(
                private_comment_reader__id=my_expert.id
            )
            notifications_count = len(all_my_private_comments)
        except:
            notifications_count = 0
    else:
        notifications_count = 0

    # Get all polities for the search bar
    all_polities = Polity.objects.all()

    # Get the search term if submitted
    search_term = request.GET.get("search", "")

    # Return the data as a dictionary
    return {
        "notifications_count": notifications_count,
        "all_polities": all_polities,
        "search_term": search_term,
    }
