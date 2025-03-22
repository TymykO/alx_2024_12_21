import requests
import aiohttp
import time
import asyncio


from django.http import JsonResponse

urls = [
    "https://jsonplaceholder.typicode.com/posts/1",
    "https://jsonplaceholder.typicode.com/posts/2",
    "https://jsonplaceholder.typicode.com/posts/3",
    "https://jsonplaceholder.typicode.com/posts/4",
    "https://jsonplaceholder.typicode.com/posts/5",
    "https://jsonplaceholder.typicode.com/posts/6",
    "https://jsonplaceholder.typicode.com/posts/7",
    "https://jsonplaceholder.typicode.com/posts/8",
    "https://jsonplaceholder.typicode.com/posts/9",
    "https://jsonplaceholder.typicode.com/posts/10",

]

def sync_example(request):
    start_time = time.time()

    results = []
    for url in urls:
        response = requests.get(url)
        results.append(response.json())

    end_time = time.time()
    return JsonResponse({
        "results": results,
        "execution_time": end_time - start_time,
    })



async def fetch_single(session, url):
    async with session.get(url) as response:
        return await response.json()


async def async_example(request):
    start_time = time.perf_counter()

    async with aiohttp.ClientSession() as session:
        posts = [fetch_single(session, url) for url in urls]
        results = await asyncio.gather(*posts)

    execution_time = time.perf_counter() - start_time
    return JsonResponse({
        "results": results,
        "execution_time": execution_time,
    })




    