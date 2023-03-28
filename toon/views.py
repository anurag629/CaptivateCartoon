# example/views.py
from datetime import datetime

from django.http import HttpResponse

def index(request):
    '''Return a simple HTML page.'''

    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello, I am Anurag Verma.</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)