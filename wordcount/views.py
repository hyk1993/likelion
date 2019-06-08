from django.shortcuts import render
from konlpy.tag import Mecab


# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def result(request):
    text = request.GET['fulltext']
    nlpy = Mecab()
    nouns = nlpy.nouns(text)
    word_dictionary = {}
    
    for word in nouns:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
    
        

    return render(request, 'result.html', {'noun': nouns, 'full': text, 'total': len(nouns), 'dictionary': word_dictionary.items()})

