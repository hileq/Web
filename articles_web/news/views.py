from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesFrom
from django.views.generic import DetailView, UpdateView, DeleteView


def news(request):
    content = {
        'news': Articles.objects.order_by('-date'),
    }
    return render(request, 'news/news.html', context=content)

class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesFrom

class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/delete_view.html'
    success_url = '/news'

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesFrom(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news')
        else:
            error = 'Wprowadzone dane były niepoprawne'

    form = ArticlesFrom()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)