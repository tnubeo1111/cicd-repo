import logging
from django.shortcuts import render
from django.http import HttpResponse


logger = logging.getLogger('django.request')

# Create your views here.
def home(request):
    response = HttpResponse("Hello App")
    logger.info(
        f"Request from {request.META.get('REMOTE_ADDR')} - "
        f"Path: {request.path} - Status: {response.status_code}"
    )
    return response

# Create a view tools for DevOps
def devops_tools(request):
    items = ['CICD', 'Monitoring', 'Logging', 'Scaling']
    html = '<h1>DevOps Tools</h1><ul>'
    for item in items:
        html += f'<li>{item}</li>'
    html += '</ul>'
    logger.info(f"DevOps tools page accessed by {request.META.get('REMOTE_ADDR')}")
    return HttpResponse(html)