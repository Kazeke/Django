from django.shortcuts import render

def index(request):
    data = { 
        'title': 'Главная страница!!!',
        'values': ['Some', 'Hello', '123'],
        'obj': { 
            'car': 'bmw',
            'age': '18',
            'hobby': 'footbal'
        }

    }
    return render(request, 'main/index.html', data)



def about(request):
    return render(request, 'main/about.html')