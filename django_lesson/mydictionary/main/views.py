from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render

def home(request):
    return render(request, 'main/home.html')

def list(request):
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    words2 = []
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)
        words2.append(word2)

    data = {
        'words': zip(words1, words2)
    }
    return render(request, 'main/list.html', data)

def add(request):
    file = open("file.txt", "r", encoding="utf-8").read().splitlines()
    words1 = []
    message = ''
    for line in file:
        word1, word2 = line.split("-")
        words1.append(word1)

    if request.method == 'POST':
        word1 = str(request.POST.get("word1"))
        word2 = str(request.POST.get("word2"))
        if word1 in words1:
            message = 'Эти слова уже есть в словаре'
        else:
            with open("file.txt", "a", encoding="utf-8") as file:
                file.write(word1 + "-" + word2 + "\n")
            return redirect('list')
    mms = {
        'message': message
    }
    return render(request, 'main/add.html', mms)