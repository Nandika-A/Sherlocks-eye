from django.shortcuts import render, HttpResponse
from django.contrib.sessions.models import Session

# Create your views here.
def index(request):
    if('car' in request.session):
        return HttpResponse('found!')
    request.session['car'] = 'Tesla'
    return HttpResponse(f'Car: {request.session["car"]}')

def get_session_data(request):
    index(request)
    sessions = Session.objects.all()
    for s in sessions:
        print(s.get_decoded())
    return HttpResponse(sessions)