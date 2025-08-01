from django.http import HttpResponse
import logging

# Setting up a logger for the application
logger = logging.getLogger('django.request')

# View for the home page
def home(request):
    logger.info(f'Home Access - From: {request.META.get("REMOTE_ADDR")}')
    return HttpResponse('<h1>Welcome to DevOps Simple Web!</h1>')


def about(request):
    logger.info(f'About Page Access - From: {request.META.get("REMOTE_ADDR")}')
    # Simulating a potential error for demonstration
    if request.GET.get('error'):
        logger.error('Simulated error on About page')
        return HttpResponse('<h2>Error: Something went wrong!</h2>', status=500)
    return HttpResponse('<h2>About: Đây là web mẫu cho DevOps!</h2>')

def jobs(request):
    logger.info(f'Jobs Page Access - From: {request.META.get("REMOTE_ADDR")}')
    items = ['CI/CD Pipeline', 'Docker', 'Kubernetes', 'Monitoring', 'Logging']
    html = "<h3>DevOps Tasks:</h3><ul>"
    for item in items:
        html += f"<li>{item}</li>"
    html += "</ul>"
    return HttpResponse(html)