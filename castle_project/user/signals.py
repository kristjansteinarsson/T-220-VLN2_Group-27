from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from user.models import User as Profile

@receiver(user_logged_in)
def create_user_profile(sender, request, user, **kwargs):
    from user.models import User as Profile
    profile, created = Profile.objects.get_or_create(auth_user=user)
    print("User profile created:", created)
    if created:
        print(f"[Signal] Created profile for user: {user.username}")
    else:
        print(f"[Signal] Profile already exists for user: {user.username}")