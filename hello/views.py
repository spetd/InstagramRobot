from django import http

def home(request):
    return http.HttpResponse('<div style=\"color:#0000FF\">Hello Worldsss!</div>')
