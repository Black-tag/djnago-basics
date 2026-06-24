from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from django.db import connection

# Create your views here.




def health(request):

    try:
        connection.ensure_connection()

        return JsonResponse({
            "status": "connection_successful",
        }, status=200)

    except Exception as e:
        return JsonResponse({
            "status": "db_not_connected",
            "error": str(e)
        }, status=503)


def index(request):
    return HttpResponse("hi this is the admin app for digicollect")