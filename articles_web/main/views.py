from django.shortcuts import render

def main(request):
    context = {
        'title': 'Strona główna',
        'values': ['Some', 'Hello', '123']
    }
    return render(request, 'main/main.html', context)

def about(request):
    return render(request, 'main/about.html', {'title': 'O nas'})