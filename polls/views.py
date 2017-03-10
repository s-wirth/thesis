from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils.timezone import now

from .forms import QuestionForm
from polls.models import Question, Option


def index(request):
    question_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))


def new_poll(request):
    if request.method == 'POST':
        new_question = QuestionForm(request.POST)
        question_text = new_question['question_text'].value()
        if new_question['pub_date'] is not None:
            pub_date = new_question['pub_date'].value()
        else:
            pub_date = now()
        new_question = Question(question_text=question_text, pub_date=pub_date)
        new_question.save()

        template = loader.get_template('polls/detail.html')
        context = {
            'question': new_question,
        }
        return HttpResponse(template.render(context, request))
    else:
        template = loader.get_template('polls/new_poll.html')
        context = {'form': QuestionForm()}
        return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")

    template = loader.get_template('polls/detail.html')
    context = {
        'question': question,
    }
    return HttpResponse(template.render(context, request))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.option_set.get(pk=request.POST['option'])
    except (KeyError, Option.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select an option.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))