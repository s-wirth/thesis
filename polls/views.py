from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.template import loader
from django.utils.decorators import method_decorator
from django.utils.timezone import now
from django.views import View

from pollgroups.models import CourseSession
from polls.models import Question, Option


def index(request):
    question_list = Question.objects.all()
    template = loader.get_template('polls/index.html')
    context = {
        'question_list': question_list,
    }
    return HttpResponse(template.render(context, request))


class CreatePollView(View):
    template = "polls/create_poll.html"

    @method_decorator(login_required)
    def post(self, request):
        question_text = request.POST['question']
        session = request.POST['session']
        new_question = Question(question_text=question_text, pub_date=now(), session=session)
        new_question.save()

        options_list = request.POST.getlist('options')
        for option in options_list:
            option_text = option
            new_option = Option(option_text=option_text, question=new_question)
            new_option.save()

        return HttpResponseRedirect(reverse('polls:detail', args=(new_question.id,)))

    def get(self, request):
        context = {'sessions': CourseSession.objects.all()}
        return render(request, self.template, context=context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except:
        raise Http404("Question does not exist")

    options = question.option_set.all().order_by('pk')

    template = loader.get_template('polls/detail.html')
    context = {
        'question': question,
        'options': options,
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
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))