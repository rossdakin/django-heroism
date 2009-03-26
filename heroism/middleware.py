from heroism import HEADER_NAME, SECURE_VALUE

class HeroismMiddleware(object):
    """
    If a specific header is present in the request, we redefine the request
    object's is_secure method to reflect whether or not the header's value
    is the specified secure protocol (e.g. "https"), defaulting to insecure.
    """
    def process_request(self, request):
        if HEADER_NAME in request.META:
            if request.META[HEADER_NAME] == SECURE_VALUE:
                request.is_secure = lambda: True
            else:
                request.is_secure = lambda: False
        return None
