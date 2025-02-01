import time
class TimeitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()
        response = self.get_response(request)
        end_time = time.time()
        request.headers["X-Time"] = f"{end_time - start_time} seconds"
        return response
