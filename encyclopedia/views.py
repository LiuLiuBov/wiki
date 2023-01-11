from http.client import HTTPResponse
from operator import truediv
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.urls import reverse
from django.shortcuts import redirect
import random

from . import util

def index(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "random_entry": random_entry
    })

def getentry(request, title):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    if(util.get_entry(title)==None):
        return render(request, 'encyclopedia/404.html', status=404)
    else:
        return render(request, "encyclopedia/page.html", {
            "page": util.get_entry(title),
            "title": title,
            "random_entry": random_entry
        })

def search(request):
    query = request.GET.get('q').lower()
    entries = util.list_entries()
    lowercase_entries = []
    for entry in entries:
          lowercase_entry = entry.lower()
          lowercase_entries.append(lowercase_entry)
    results = [word for word in lowercase_entries if query in word]
    print(results)
    if query in lowercase_entries:
        return HttpResponseRedirect(f'/wiki/{query}')
    for entry in lowercase_entries:
        if query in entry:
            return render(request, 'encyclopedia/search_results.html',{
                "results": results
            })
    return render(request, 'encyclopedia/404.html', status=404)


def create(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    if request.method == 'POST':
        text = request.POST['text']
        title = request.POST['title']
        entries = util.list_entries()
        lowercase_entries = []
        for entry in entries:
               lowercase_entry = entry.lower()
               lowercase_entries.append(lowercase_entry)
        if title.lower() in lowercase_entries:
            return render(request, "encyclopedia/create.html", {'error': 'A file with the provided title already exists. Please choose a different title.'})
        # Save the markdown text to a file
        with open(f'entries/{title}.md', 'w') as file:
            file.write(text)
        return HttpResponseRedirect(f'/wiki/{title}')
    else:
        return render(request, "encyclopedia/create.html",{
            "random_entry": random_entry
        })

def edit(request, title):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    if request.method == 'POST':
        text = request.POST['text']
        with open(f'entries/{title}.md', 'w') as file:
            file.write(text)
        return HttpResponseRedirect(f'/wiki/{title}')
    else:
        return render(request, "encyclopedia/edit.html",{
            "title": title,
            "page": util.get_entry(title),
            "random_entry": random_entry
        })

def randomize(request):
    entries = util.list_entries()
    random_entry = random.choice(entries)
    return render(request, "encyclopedia\layout.html", {
        "random_entry": random_entry
    })
