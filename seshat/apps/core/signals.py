from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import SeshatCommentPart


@receiver(post_save, sender=SeshatCommentPart)
def update_subcomment_ordering(sender, instance, **kwargs):
    """
    A signal to update the ordering of subcomments when a new subcomment is
    created or an existing subcomment is updated.

    Args:
        sender (SeshatCommentPart): The sender of the signal.
        instance (SeshatCommentPart): The instance of the subcomment.
        **kwargs: Arbitrary keyword arguments.

    Returns:
        None
    """
    if not instance.pk:
        last_subcomment = instance.comment.inner_comments_related.last()
        instance.comment_order = (
            last_subcomment.comment_order + 1 if last_subcomment else 0
        )

        SeshatCommentPart.objects.filter(pk=instance.pk).update(
            comment_order=instance.comment_order
        )
    else:
        # Re-order all the subcomments if the order of the current subcomment has changed
        comment_order = instance.comment_order
        subcomments = (
            instance.comment.inner_comments_related.filter(
                comment_order__gte=comment_order
            )
            .exclude(pk=instance.pk)
            .order_by("comment_order")
        )
        subcomments.update(comment_order=F("comment_order") + 1)
