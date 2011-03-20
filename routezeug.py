'''

Routezeug -- minimally useful routing for werkzeug

Example::

    import routezeug
    import werkzeug
    import wsgiref.simple_server


    def index(request):
        return werkzeug.Response('Index\n')

    def photo(request, photo_id):
        return werkzeug.Response('Photo: %s\n' % photo_id)


    application = routezeug.router(
        ('/',          index),
        ('/:photo_id', photo),
    )

    server = wsgiref.simple_server.make_server('', 8000, application)
    server.serve_forever()

'''


import re

import werkzeug
import werkzeug.exceptions


__all__ = ['router']

def make_route(route_spec):
    path, handler = route_spec
    pattern = '^' + re.sub(r':(\w+)', r'(?P<\1>[\w-]+)', path) + '$'
    return (re.compile(pattern), handler)


def router(*patterns):
    routes = map(make_route, patterns)

    @werkzeug.Request.application
    def application(request):
        for (regex, handler) in routes:
            match = regex.match(request.path)
            if match:
                return handler(request, **match.groupdict())
        return werkzeug.exceptions.NotFound()

    return application
