from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Venues
from users.models import UserType


@receiver(post_save, sender=Venues)
def update_user_type(sender, instance, created, **kwargs):
    if created:
        print(instance.owner, "created")
        instance.owner.role = UserType.PROVIDER
        instance.owner.save()
