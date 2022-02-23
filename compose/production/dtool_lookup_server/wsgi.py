"""Create dtool_lookup_server wsgi app."""
import os
import pprint
from dtool_lookup_server import create_app

app = create_app()

# wrap logging middleware if DUMP_HTTP_REQUESTS set true
if os.getenv("DUMP_HTTP_REQUESTS", 'False').lower() in ('true', '1', 't'):
    class LoggingMiddleware:
        """Wrap wsgi app and dump all requests."""

        def __init__(self, app):
            self._app = app

        def __call__(self, env, resp):
            errorlog = env['wsgi.errors']
            pprint.pprint(('REQUEST', env), stream=errorlog)

            def log_response(status, headers, *args):
                pprint.pprint(('RESPONSE', status, headers), stream=errorlog)
                return resp(status, headers, *args)
            return self._app(env, log_response)
    app = LoggingMiddleware(app)
