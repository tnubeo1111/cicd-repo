from django.http import HttpResponse
import logging

# Setting up a logger for the application
logger = logging.getLogger('django.request')

# View for the home page
def home(request):
    logger.info(f'Home Access - From: {request.META.get("REMOTE_ADDR")}')
    return HttpResponse('<h1>Welcome to DevOps Simple Web!</h1>')

def jobs(request):
    logger.info(f'Jobs Page Access - From: {request.META.get("REMOTE_ADDR")}')
    items = ['CI/CD Pipeline', 'Docker', 'Kubernetes', 'Monitoring', 'Logging']
    html = "<h3>DevOps Tasks:</h3><ul>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ul>"
    return HttpResponse(html)