import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger('django.request')

# Create your views here.
def hello(request):
    response = HttpResponse("Hello App")
    logger.info(
        f"Request from {request.META.get('REMOTE_ADDR')} - "
        f"Path: {request.path} - Status: {response.status_code}"
    )
    return response