from django.shortcuts import render, HttpResponse
from .decorators import not_banned
#from django.contrib.sessions.models import Session

# Create your views here.
@not_banned
def test_emotions(request):
    request.session["emotion"] = "happy"
    #request.session["emotion"] = "disturbing"
    check_for_ban(request)
    return HttpResponse("You are banned")

def check_for_ban(request):
    if request.session["emotion"] == "disturbing" or request.session["emotion"] == "violent":
        request.session["banned"] = False
        return HttpResponse("You are banned")
    
def index(request):
    if('car' in request.session):
        return HttpResponse('found!')
    request.session['car'] = 'Tesla'
    return HttpResponse(f'Car: {request.session["car"]}')

def get_session_data(request):
    from django.contrib.sessions.models import Session
    index(request)
    sessions = Session.objects.all()
    for s in sessions:
        print(s.get_decoded())
    #return HttpResponse(sessions)
    #return HttpResponse("Emotion set to happy")
    return render(request, 'main.html')

def get_llm_output(text_data):

    #dummy info
    return text_data[0]

def get_llm_anim_no(text_data):
    return 1
