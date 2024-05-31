from django import template
from social_django.models import UserSocialAuth

register = template.Library()

@register.filter
def is_google_backend(user):
    if user.is_authenticated:
        return UserSocialAuth.objects.filter(user=user, provider='google-oauth2').exists()
    return False