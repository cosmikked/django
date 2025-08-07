from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.db.models import F
from django.urls import reverse

from .models import Question, Choice

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
    # try:
    #     question = Question.objects.get(pk=question_id) 
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist.")
    # return render(request, "polls/detail.html", {"question": question})

    # shortcut version
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        # retrieves the Choice object submitted in the voting form in detail.html
        # choice.id is primary key because it is the value of the radio field 
        choice = question.choice_set.get(pk=request.POST['choice']) 
    # catches if a choice object is not retrieved
    # DoesNotExist is automatically created by django for every model
    except (KeyError, Choice.DoesNotExist):
        return render(
            request, "polls/detail.html", {
                "question": question,
                "error_message": "You did not vote on any choice."
            }
        )
    else: 
        # F instructs the db to increment the votes field by 1 without loading the field data into python memory
        choice.votes = F("votes") + 1
        choice.save()

        # reverse returns a url string
        return HttpResponseRedirect(reverse("polls:results", args=(question_id, )))
