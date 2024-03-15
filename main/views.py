from django.shortcuts import render, HttpResponse

# Create your views here.
def test_emotions(request):
    request.session["emotion"] = "happy"
    #return HttpResponse("Emotion set to happy")
    return render(request, 'main.html')

def get_llm_output(text_data):

    #dummy info
    return text_data[0]

def get_llm_anim_no(text_data):
    return 1