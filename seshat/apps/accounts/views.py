from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView

from .models import Profile, Seshat_Expert, Seshat_Task
from .forms import Seshat_TaskForm, ProfileForm, CustomSignUpForm

from ..core.models import SeshatPrivateCommentPart


def accounts(request):
    """
    View function for the accounts page.

    Note:
        TODO: This seems like an unused function and it should be removed.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return HttpResponse("<h1>Hello Accounts.</h1>")


def accounts_new(request):
    """
    View function for the accounts page.

    Note:
        TODO: This seems like an unused function and it should be removed.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    return HttpResponse("<h1>Hello Aiiiiiiiccounts.</h1>")


def has_add_scp_prv_permission(user):
    """
    Function to check if a user has the 'core.add_seshatprivatecommentpart' permission.

    Note:
        TODO: Investigate whether this function doubles with the functionality
        of the 'permission_required' decorator.

    Args:
        user (User): The user object.

    Returns:
        bool: True if the user has the permission, False otherwise.
    """
    return user.has_perm("core.add_seshatprivatecommentpart")


class ProfileUpdate(PermissionRequiredMixin, UpdateView):
    """
    Generic class-based view for updating a user's profile.
    """

    model = Profile
    context_object_name = "user"
    form_class = ProfileForm
    template_name = "registration/profile_update.html"
    queryset = Profile.objects.all()
    permission_required = "core.add_seshatprivatecommentpart"

    def get_context_data(self, **kwargs):
        """
        Get the context data of the view.

        :noindex:

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: The context data of the view.
        """
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        user = self.request.user
        context["profile_form"] = ProfileForm(
            instance=self.request.user.profile,
            initial={"first_name": user.first_name, "last_name": user.last_name},
        )
        return context

    def form_valid(self, form):
        """
        Method for saving the form data.

        Args:
            form (Form): The form object.

        Returns:
            HttpResponseRedirect: The response object.
        """
        profile = form.save()
        user = profile.user
        user.last_name = form.cleaned_data["last_name"]
        user.first_name = form.cleaned_data["first_name"]
        user.save()
        return HttpResponseRedirect(reverse_lazy("user-profile"))


@login_required
@permission_required("core.add_seshatprivatecommentpart", raise_exception=True)
def profile(request):
    """
    View function for displaying a user's profile.

    Note:
        This view requires that the user be logged in.
        This view requires that the user have the 'core.add_seshatprivatecommentpart' permission.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    all_facts = 0
    all_tasks_given = []
    user_profile_id = None
    if request.user.is_authenticated:
        user_profile_id = request.user.profile.id
    my_user = Profile.objects.get(pk=user_profile_id)
    my_expert = Seshat_Expert.objects.get(user_id=request.user.id)
    print(f"my_profile_id: {user_profile_id}")
    print(f"my_user_id: {request.user.id}")

    all_my_private_comments = SeshatPrivateCommentPart.objects.filter(
        private_comment_reader__id=my_expert.id
    )
    print(f"my_expert_id: {my_expert.id}")

    context = {
        "facts_verified_by_user": all_my_private_comments,
        "all_facts": all_facts,
        "all_tasks_given": all_tasks_given,
    }

    print(my_user)
    return render(request, "registration/profile.html", context=context)


class Seshat_taskCreate(PermissionRequiredMixin, CreateView):
    """
    Generic class-based view for creating a task.
    """

    model = Seshat_Task
    form_class = Seshat_TaskForm
    template_name = "registration/seshat_task/seshat_task_form.html"
    permission_required = "core.add_seshatprivatecommentpart"


class Seshat_taskDetailView(generic.DetailView):
    """
    Generic class-based detail view for a task.
    """

    model = Seshat_Task
    template_name = "registration/seshat_task/seshat_task_detail.html"


def signup(request):
    """
    View function for signing up a new user.

    Note:
        This view function handles both GET and POST requests.

    Args:
        request (HttpRequest): The request object.

    Returns:
        HttpResponse: The response object.
    """
    if request.method == "POST":
        form = CustomSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Authenticate the user
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect("home")  # Replace 'home' with your desired redirect URL
    else:
        form = CustomSignUpForm()

    return render(request, "signup.html", {"form": form})
