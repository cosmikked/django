from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader

from .models import Question

# Create your views here.


# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     template = loader.get_template("polls/index.html") 
#     # creates a dictionary of the question data
#     # context must always be a dictionary, it maps variable names to Python object which the template can refer to 
#     context = {"latest_question_list": latest_question_list}
#     # render fills the template with the data from the context
#     return HttpResponse(template.render(context, request))

# shortcut way of loading and rendering templates
def index(request):
    latest_question_list = Question.objects.order_by("pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    # returns an HttpResponse object
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id) 
    except Question.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    result = "You're looking at the results of question %s."
    return HttpResponse(result % question_id)

def vote(request, question_id):
    