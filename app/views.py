"""
Definition of views.
"""
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from twilio.rest import TwilioRestClient


#from django_twilio.utils import discover_twilio_credentials
#import twilio
#import twilio.rest

#from django.contrib.auth.models import User

#from django_twilio.client import twilio_client

numberlist=[]
citylist=[]

YOUR_INFO = {
    'name' : 'Notyfy',
    'bio' : 'Community Driven Alerts.',
    'email' : '', # Leave blank if you'd prefer not to share your email with other conference attendees
    
    'headshot_url' : 'http://i.imgur.com/5L7ofip.png?1', # Link to your GitHub, Twitter, or Gravatar profile image.
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
        message1 = 'The number %s has been added to get alerts from the city of %s' % (request.GET['number'], request.GET['city'])
        message2 = 'You can unsubscribe from this service at anytime.'
        numberlist.append(request.GET['number'])
        citylist.append(request.GET['city'].lower())
    else:
        message = 'You entered nothing.'
    return render(
        request,
        'app/append.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,
                'thanks' : message2,
                'message' : message1,        
        })
    )
    

def broadcast(request):
    
    
    ACCOUNT_SID = "ACfa54a756a82c32aa2d643e6f72fd14c5" 
    AUTH_TOKEN = "985442a038ab0c3757277de82142962f" 
     
    client = TwilioRestClient(ACCOUNT_SID, AUTH_TOKEN) 

    text = request.GET['message']
    location = request.GET['city2']
    location = location.lower()

    for x in range (0 , len(citylist)):
        if citylist[x]==location:
            client.messages.create(to=numberlist[x], from_='+16103475940', body=text)
    

    if 'city2' in request.GET and 'message' in request.GET:
        message1 = "Thank you for keeping your city safe."
        message2 = 'Your alert has been sent.'
    return render(
        request,
        'app/append.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,
                'thanks' : message2,
                'message' : message1,        
        })
    )

def cancel(request):

    number = request.GET['number2']
    message1 = "The entered number is not in our directory."
    message2 = "Please retry."

    for x in range (0, len(numberlist));
        if number == numberlist[x]:
            del numberlist[x]
            del citylist[x]
            message1 = "You have unsubscribed successfully."
            message2 = "Thank you."
             

    return render(
        request,
        'app/append.html',
        context_instance = RequestContext(request,
            {
                'attendee' : YOUR_INFO,
                'thanks' : message2,
                'message' : message1,        
        })
    )

