from django.shortcuts import render
from django.contrib.sessions.models import Session

# Create your views here.

def get_emotions():
    """
    Function that returns the dictionary of emotions v/s count for all the user sessions in the database
    This can be used to plot the graph.
    """
    session = Session.objects.all()
    emotions = {'happy': 0, 'sad': 0, 'angry': 0, 'fearful': 0, 'disgusted': 0, 'surprised': 0, 'neutral': 0}
    for s in session:
        if 'emotion' in s.get_decoded():
            emotions[s.get_decoded()['emotion']] += 1
    # print(emotions)
    return emotions

def admin_page(request):
    """
    Function that renders the admin page and passes the emotions dictionary to plot the graph
    """
    emotions = get_emotions().items()
    return render(request, 'admin_page/admin_page.html', {"emotions": emotions})

def get_chats():
    """
    Function that returns the chat history for different user sessions
    """
    pass