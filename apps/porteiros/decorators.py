from functools import wraps

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def porteiro_required(view_func):
    """Allow access only to authenticated users with a porter profile."""

    @login_required
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not hasattr(request.user, "porteiro"):
            return redirect("completar_cadastro_porteiro")
        return view_func(request, *args, **kwargs)

    return wrapper
