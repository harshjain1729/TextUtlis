# I have created this file.
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    dict = {'name': 'Harsh Jain', 'College': 'BU'}
    return render(request, 'index.html', dict)


def analyzer(request):
    recievedText = request.GET.get('analysedText', 'default')
    punctuationChecker = request.GET.get('punctuationChecker', 'default')
    capitalizeChecker = request.GET.get('capitalizer', 'default')
    newLineRemover = request.GET.get('newLineRemover', 'default')
    extraSpaceRemover = request.GET.get('extraSpaceRemover', 'default')
    print(newLineRemover)
    print(recievedText)
    if punctuationChecker=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in recievedText:
            if char not in punctuations:
                analyzed = analyzed+char
        dict = {'analysed_text': analyzed,
                'comments': 'All the punctuations from your text has been removed by Django.'}
        return render(request, "analyze.html", dict)
    elif capitalizeChecker=='on':
        analyzed = ""
        for char in recievedText:
            analyzed = analyzed+char.upper()
        dict = {'analysed_text': analyzed,
                'comments': 'All the characters from your text has been converted in uppercase by Django.'}
        return render(request, "analyze.html", dict)
    elif newLineRemover=='on':
        analyzed = ""
        for char in recievedText:
            if char!="\n":
                analyzed = analyzed+char
        dict = {'analysed_text': analyzed,
                'comments': 'All the next lines from your text has been removed by Django.'}
        return render(request, "analyze.html", dict)
    elif extraSpaceRemover == "on":
        analyzed = ""
        for index, char in enumerate(recievedText):
            if not (recievedText[index] == " " and recievedText[index + 1] == " "):
                analyzed = analyzed + char

        dict = {'analysed_text': analyzed,
                'comments': 'All the extra spaces from your text has been removed by Django.'}
        return render(request, "analyze.html", dict)
    else:
        return HttpResponse("Error")





