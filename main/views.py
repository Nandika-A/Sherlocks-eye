from django.shortcuts import render, HttpResponse

# Create your views here.
def test_emotions(request):
    request.session["emotion"] = "happy"
    return HttpResponse("Emotion set to happy")