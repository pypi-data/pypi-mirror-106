from datetime import datetime

from django.conf import settings
from django.http import FileResponse, Http404, HttpRequest
from django.views import View

from .storage import TitofistoStorage

_DEFAULT_PARAM_PREFIX = "titofisto_"
_DEFAULT_TIMEOUT = 60 * 60


class TitofistoMediaView(View):
    def get(self, request: HttpRequest, name: str) -> FileResponse:
        # Get storage and determine settings
        storage = TitofistoStorage()
        param_prefix = getattr(settings, "TITOFISTO_PARAM_PREFIX", _DEFAULT_PARAM_PREFIX)

        # Inspect URL parameters for completeness
        ts = request.GET.get(f"{param_prefix}ts", None)
        token = request.GET.get(f"{param_prefix}token", None)
        if ts is None or token is None:
            raise Http404()

        # Compute expected token for filename
        try:
            expected_token, _ = storage.get_token(name, ts)
        except FileNotFoundError:
            raise Http404()

        # Compare tokens and raise 404 if they do not match
        if expected_token != token:
            raise Http404()

        # Calculate time difference if timeout is set
        now = datetime.now().strftime("%s")
        timeout = getattr(settings, "TITOFISTO_TIMEOUT", _DEFAULT_TIMEOUT)
        if timeout is not None and int(now) - int(ts) > timeout:
            raise Http404()

        # Finally, serve file from disk if all checks passed
        return FileResponse(storage._open(name))
