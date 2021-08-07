from django.shortcuts import render
# Create your views here.

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
    questions = Question.objects.order_by('-id')

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


    tags = Tag.objects.all()

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
