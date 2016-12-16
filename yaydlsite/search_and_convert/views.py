from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader

# Youtube Search API stuff





# Called on GET /
def index(request):
    return render(request, 'search_and_convert/search.html')

# Called on "Search" button click
def search(request):
    # if (request.GET.get('searchBtn')):
    #    print('user click!')
    #    return HttpResponse("y halo thar")
    #    return 'hey'
    #    searchBtn = "hey"
    return HttpResponse("Search")


#
# def select(request):
#     return HttpResponse("Select")
#
# def convert(request):
#     return HttpResponse("Convert")




# from django.shortcuts import render, get_object_or_404
# from django.http import HttpResponse, Http404
# from django.template import loader
#
# from .models import Question
#
# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     #template = loader.get_template('polls/index.html')
#     context = { 'latest_question_list': latest_question_list, }
#     #return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context)
#
# def detail(request, question_id):
#     #try:
#     #    question = Question.objects.get(pk=question_id)
#     #except Question.DoesNotExist:
#     #    raise Http404("Question does not exist")
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})
#     #return HttpResponse("You're looking at question %s." % question_id)
#
# def results(request, question_id):
#     return HttpResponse("You're looking at the results of question %s." % question_id)
#
# def vote(request, question_id):
#     return HttpResponse("You're voting on question %s." % question_id)
