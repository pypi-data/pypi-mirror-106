from json import dumps

from ..gates.catch_all import Gate
from ..gates.units import SECONDS
from ..gates.util import raise_package_error

try:
    from fastapi import Request
    from fastapi.responses import Response
except ImportError:
    raise_package_error("fastapi")


error = dumps(
    {"error": "You have been rate limited, try again in %S% seconds"}
).encode()


def default_error_response(t):
    x = f"{int(t)}"
    return Response(
        error.replace(b"%S%", x.encode()),
        status_code=429,
        headers={"x-rate-limit": "1", "x-time-left": x},
    )


def guard(
    request_count=10,
    *,
    per=3,
    units=SECONDS,
    limit_response=default_error_response,
    ip_resolver="heroku",
    ban_time=0,
):
    time_interval = per * units

    kwargs = {
        "per": time_interval,
        "units": units,
        "request_count": request_count,
        "ban_time": ban_time,
        "ip_resolver": ip_resolver,
    }

    guard = Gate(**kwargs)

    async def middleware(request: Request, call_next):
        is_banned, time_left = guard.guard(request)
        if is_banned:
            return limit_response(time_left)
        return await call_next(request)

    return middleware
