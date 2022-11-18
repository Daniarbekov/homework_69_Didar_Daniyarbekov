from django.shortcuts import render
import json
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponse, HttpResponseNotAllowed, JsonResponse
# Create your views here.


@ensure_csrf_cookie
def get_token(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(f'Not allowed Method {request.method}')


def index(request):
    return render(request, 'index.html')


def add(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            a = float(data.get('A'))
            b = float(data.get('B'))
            response = JsonResponse({'answer': round(a + b , 1)})
        except ValueError:
            response = JsonResponse({"error": "Incorrect data"})
            response.status_code = 400
        return response


def multiply(request, *args, **kwargs):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            a = float(data.get('A'))
            b = float(data.get('B'))
            response = JsonResponse({'answer': round(a * b, 1)})
        except ValueError:
            response = JsonResponse({"error": "Incorrect data"})
            response.status_code = 400
        return response
