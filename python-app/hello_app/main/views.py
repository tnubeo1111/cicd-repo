import logging
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.http import require_GET


logger = logging.getLogger('django.request')

# Create your views here.
@require_GET
def hello(request):
    response = HttpResponse("Hello App")
    logger.info(
        f"Request from {request.META.get('REMOTE_ADDR')} - "
        f"Path: {request.path} - Status: {response.status_code}"
    )
    return response