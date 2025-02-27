# Alexandria/home/views.py

from django.shortcuts import render

def sample(request):
    data = {
        'books':[
            {
                'title':"Frankenstein",
                'author':"Shelley, Mary",
            },
            {
                'title':"Metamorphosis",
                'author':"Kafka, Franz",
                'recommended':True,
            },
            {
                'title':"Dracula",
                'author':"Stoker, Bram",
                'recommended':False,
            },
        ]
    }

    return render(request, "sample.html", data)

def sample_my(request):
    data = {
        'books':[
            {
                'title':"Matrix",
                'author':"Shelley, Mary",
            },
            {
                'title':"Matric Resurections",
                'author':"Kafka, Franz",
                'recommended':True,
            },
            {
                'title':"catrix",
                'author':"Stoker, Bram",
                'recommended':False,
            },
        ]
    }

    return render(request, "sample.html", data)

def about(request):
    return render(request, "about.html")


def home(request):
    return render(request, "home.html")
