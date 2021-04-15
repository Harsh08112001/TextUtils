from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request, "index.html")


def analyze(request):
    # Get the text
    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    capitalizefirst = request.GET.get('capitalizefirst', 'off')
    newlineremove = request.GET.get('newlineremove', 'off')
    spaceremove = request.GET.get('spaceremove', 'off')
    charcount = request.GET.get('charcount', 'off')
    email = request.GET.get('email', 'off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif capitalizefirst == "on":
        analyzed = ""
        analyzed = djtext.title()
        params = {'purpose': 'Capitalized First', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)

    elif newlineremove == "on":
        analyzed = ""
        analyzed = djtext.rstrip()
        params = {'purpose': 'New Line Remove', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif spaceremove == "on":
        analyzed = ""
        analyzed = djtext.replace(" ", "")
        params = {'purpose': 'Space Remove', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif charcount == "on":
        analyzed = len(djtext)
        params = {'purpose': 'Space Remove', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    elif email == "on":
        analyzed = djtext
        analyzed = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", analyzed)
        params = {'purpose': 'extarct email', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('Error')

# def removepunc(request):
#     djtext=request.GET.get("text","default")
#     print(djtext)
#     return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("capitalize first")

# def spaceremove(request):
#     return HttpResponse("space remover")

# def charcount(request):
#     return HttpResponse("charcount ")
