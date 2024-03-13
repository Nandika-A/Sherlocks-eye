from django.shortcuts import render, HttpResponse

def not_banned(func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get("banned", False):
            return func(request, *args, **kwargs)
        else:
            raise Exception("This user is banned.")
    return wrapper