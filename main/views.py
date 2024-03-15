from django.shortcuts import render, HttpResponse
from .decorators import not_banned
# Create your views here.
@not_banned
def test_emotions(request):
    request.session["emotion"] = "happy"
    #request.session["emotion"] = "disturbing"
    check_for_ban(request)
    return HttpResponse("You are")

def check_for_ban(request):
    if request.session["emotion"] == "disturbing" or request.session["emotion"] == "violent":
        request.session["banned"] = True
        return HttpResponse("You are banned")
    