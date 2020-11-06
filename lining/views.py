from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index2.html')

def blog(request):
    return render(request, 'Blog.html')

def about(request):
    return render(request, 'about.html')

def contactus(request):
    djtext = request.POST.get('text', 'default')  # get the text  # using post to  post the data in the server
    remove_pun = request.POST.get('remove_pun', 'off')
    caps = request.POST.get('caps', 'off')
    new_line_rem = request.POST.get('new_line_rem', 'off')
    extra_space_remover = request.POST.get('extra_space_remover', 'off')
    char_count = request.POST.get('char_count', 'off')

    if remove_pun == 'on':
        punctuations = ''' "!@#$%^&*()_+|}P'/.,';[]_=:>?<| '''
        analyzed = ''
        for char in djtext:
            if char not in punctuations:
                analyzed += char

        params = {'purpose': 'remove punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    if caps == 'on':
        analyzed = ''
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Your text has capitalized', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    if new_line_rem == 'on':
        analyzed = ''
        for char in djtext:
            if char != '\n' and char != '\r':
                analyzed += char
        params = {'purpose': 'New lines removed', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    if extra_space_remover == 'on':
        analyzed = ''
        for index, char in enumerate(djtext):
            if not(djtext[index] == '' and djtext[index + 1] == ''):
                analyzed += char
        params = {'purpose': 'Extra Spaces removed', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    if char_count == 'on':
        analyzed = ''
        for char in djtext:
            analyzed = len(djtext)
        params = {'purpose': 'No of characters in the Sting below', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)


    if remove_pun != 'on' and caps != 'on' and new_line_rem != 'on' and extra_space_remover != 'on':
     return HttpResponse("Error")