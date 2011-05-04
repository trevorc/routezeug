Routezeug
=========

*minimally useful routing for werkzeug*

Example:

    import routezeug
    import werkzeug
    import wsgiref.simple_server


    def index(request):
        return werkzeug.Response('Index\n')

    def photo(request, photo_id):
        return werkzeug.Response('Photo: %s\n' % photo_id)


    application = routezeug.router(
        ('GET', '/',          index),
        ('*',   '/:photo_id', photo),
    )

    server = wsgiref.simple_server.make_server('', 8000, application)
    server.serve_forever()

