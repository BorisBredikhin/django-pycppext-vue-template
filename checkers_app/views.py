import json

from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import User
# Create your views here.

def apply(f, *args, **kwargs):
    return f(*args, **kwargs)

def register(request: HttpRequest) -> JsonResponse:
    login, password = apply(lambda d: (d['login'], d['password']), json.loads(request.body))
    new_user = User.objects.create_user(login, password=password)
    new_user.save()
    return JsonResponse({"token":0}) # TODO: create token