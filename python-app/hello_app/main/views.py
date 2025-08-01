import logging
from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger('django.request')

def home(request):
    response = HttpResponse("Hello App")
    ip = request.META.get('REMOTE_ADDR', 'Unknown IP')
    logger.info(
        f"Request from {ip} - Path: {request.path} - Status: {response.status_code}"
    )
    return response
