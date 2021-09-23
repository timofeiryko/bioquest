from django.shortcuts import render
from .models import Topic, Tag, Question, VarList, Relative, RelInitial
from django.core.paginator import Paginator
# Create your views here.

@csrf_exempt
def update(request):
    if request.method == "POST":
        '''
        pass the path of the diectory where your project will be
        stored on PythonAnywhere in the git.Repo() as parameter.
        Here the name of my directory is "test.pythonanywhere.com"
        '''
        repo = git.Repo("newbioquest.pythonanywhere.com/")
        origin = repo.remotes.origin

        origin.pull()

        return HttpResponse("Updated code on PythonAnywhere")
    else:
        return HttpResponse("Couldn't update the code on PythonAnywhere")

def index(request):
    return render(request, 'about.html')

def about(request):
    return render(request, 'about.html')

def add(request):
    return render(request, 'add.html')

def instructions(request):
    return render(request, 'instructions.html')

def personal(request):
    return render(request, 'personal.html')

def problems(request):

    search = request.GET.get('search', '')
    questions = Question.objects.order_by('-id')
    tags = Tag.objects.all()
    topic = request.GET.get('topic', '')

    paginator = Paginator(questions, 20)
    page_number = request.GET.get('page', 1)
    page = paginator.get_page(page_number)

    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''


    context = {
        'title': 'Вопросы',
        'questions': page, 'tags': tags,
        'is_paginated': is_paginated,
        'next_url': next_url,
        'prev_url': prev_url,
        'search': search,
        'topic': topic
        }
    return render(request, 'problems.html', context = context)
