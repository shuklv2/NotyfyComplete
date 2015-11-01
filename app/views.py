﻿"""
Definition of views.
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

YOUR_INFO = {
    'name' : 'Notyfy',
    'bio' : 'Community Inputed Alerts.',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    'twitter_username' : 'Notyfy', # No @ symbol, just the handle.
    'github_username' : "Notyfy", 
    'headshot_url' : '', # Link to your GitHub, Twitter, or Gravatar profile image.
}
    
def home(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/base.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,    
                'year': datetime.now().year,
        
    )

def append(request):
    message=''
    if 'number' in request.GET and 'city' in request.GET:
        message = 'You entered %s and %s' % (request.GET['number'], request.GET['city'])
    else if request.GET['number']=='' or request.GET['city']=='':
        message = 'You entered nothing.'
    return HttpResponse(message)

def broadcast(request):
    message=''
    if 'city2' in request.GET and 'message' in request.GET:
        message = 'Sending text to %s saying %s' % (request.GET['city2'], request.GET['message'])
    return HttpResponse(message)


