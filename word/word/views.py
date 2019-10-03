# from django.http import HttpResponse
import operator

from django.shortcuts import render


def homepage(request):
    # print(request) the request is a GET request

    # return HttpResponse('<h1>Welcome to Django</h1>')

    # to pass html file you don't use httpresponse, youuse render


    studentList = ['John', 'Paul', 'Patrick']
    context =  {'name': 'Django',
                'greeting': 'Good evening',
                'list': studentList
                }


    return render(request, 'home.html', context)


def countPage(request):
    words = request.POST['plainText']
    wordlist = words.split() # turn each word into a list
    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] +=1
        else:
            worddictionary[word] = 1


    context = {
        'count': len(wordlist),
        'fulltext': words,
        'worddictionary': sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
    }




    print(wordlist)
    return  render(request, 'count.html', context)
