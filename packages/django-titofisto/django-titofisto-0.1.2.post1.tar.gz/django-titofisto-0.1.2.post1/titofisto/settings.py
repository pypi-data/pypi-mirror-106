from django.conf import settings

PARAM = getattr(settings, "TITOFISTO_PARAM", "titofisto_token")
TIMEOUT = getattr(settings, "TITOFISTO_TIMEOUT", 60 * 60)
