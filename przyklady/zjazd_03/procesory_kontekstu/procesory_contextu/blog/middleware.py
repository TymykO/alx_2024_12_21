import logging

import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class TimeitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time.time()

        response = self.get_response(request)
        
        end_time = time.time()
        response["X-Time"] = f"{end_time - start_time} seconds"
        logger.info(f"Time taken: {end_time - start_time} seconds")
        return response


# logować request.method i request.path
# logowa response.status_code