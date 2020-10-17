from django.shortcuts import render
import operator
def home(request):


    return render(request,'home.html')
def count(request):
    fulltext = request.GET['fulltext']
    wordlist=fulltext.split()
    wordset={}
    for word in wordlist:
        if word in wordset:
            wordset[word] += 1
        else:
            wordset[word] = 1
    sortinglist=sorted(wordset.items(),key=operator.itemgetter(1),reverse=True)
    return render(request,'count.html',{ 'fulltext': fulltext,'cuntsword':len(wordlist),'wordset': sortinglist})
def about(request):


    return render(request,'about.html')