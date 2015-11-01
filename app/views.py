"""
Definition of views.
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
#from twilio.rest import TwilioRestClient 
from django_twilio.client import twilio_client


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
        })
    )

def append(request):
    message=''
    if 'number' in request.GET and 'city' in request.GET:
        message = 'You entered %s and %s' % (request.GET['number'], request.GET['city'])
    else:
        message = 'You entered nothing.'
    return HttpResponse(message)

def broadcast(request):

    ACCOUNT_SID = "ACfa54a756a82c32aa2d643e6f72fd14c5" 
    AUTH_TOKEN = "985442a038ab0c3757277de82142962f" 
     
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 
    
    text = request.GET['message']
    location = request.GET['city2']
    location.lower()
    
    client.messages.create(to=location, from_='+16103475940', body=text)
        



   # message=''
    #if 'city2' in request.GET and 'message' in request.GET:
    #    message = 'Sending text to the city of %s saying %s' % (request.GET['city2'], request.GET['message'])
    #return HttpResponse(message)


