from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    TemplateView,
    UpdateView,
)

from ..core.models import SeshatPrivateCommentPart

from .models import Profile, Seshat_Expert, Seshat_Task
from .forms import Seshat_TaskForm, ProfileForm


class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
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
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)

        # Add the profile form to the context
        context["profile_form"] = ProfileForm(
            instance=self.request.user.profile,
            initial={
                "first_name": self.request.user.first_name,
                "last_name": self.request.user.last_name,
            },
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

        # Update the user object
        user = profile.user
        user.last_name = form.cleaned_data["last_name"]
        user.first_name = form.cleaned_data["first_name"]
        user.save()

        return HttpResponseRedirect(reverse_lazy("user-profile"))


class Profile(PermissionRequiredMixin, TemplateView):
    template_name = "registration/profile.html"
    permission_required = "core.add_seshatprivatecommentpart"

    def get_context_data(self, **kwargs) -> dict:
        context = {
            "facts_verified_by_user": [],
            "all_facts": 0,
            "all_tasks_given": [],
        }

        try:
            # Get the expert object for the logged in user
            expert = Seshat_Expert.objects.get(user_id=self.request.user.id)
        except Seshat_Expert.DoesNotExist:
            pass
        else:
            context["facts_verified_by_user"] = (
                SeshatPrivateCommentPart.objects.filter(
                    private_comment_reader__id=expert.id
                )
            )

        return context


class Seshat_TaskCreateView(PermissionRequiredMixin, CreateView):
    """
    Generic class-based view for creating a task.
    """

    model = Seshat_Task
    form_class = Seshat_TaskForm
    template_name = "registration/seshat_task/seshat_task_form.html"
    permission_required = "core.add_seshatprivatecommentpart"


class Seshat_TaskDetailView(DetailView):
    """
    Generic class-based detail view for a task.
    """

    model = Seshat_Task
    template_name = "registration/seshat_task/seshat_task_detail.html"
