from django.shortcuts import redirect

def hello_world(request):
    return redirect('/static/imgmap.html')
