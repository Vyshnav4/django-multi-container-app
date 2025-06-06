from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Choice, Question


# This view displays a list of the latest 5 questions.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """
        Return the last five published questions (not including those set to be
        published in the future).
        """
        return Question.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


# This view displays a specific question and its choices.
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Question.objects.filter(pub_date__lte=timezone.now())


# This view displays the results for a specific question.
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


# This function handles the voting for a particular choice on a question.
def vote(request, question_id):
    # Get the question object or return a 404 error if it doesn't exist.
    question = get_object_or_404(Question, pk=question_id)
    try:
        # Get the selected choice from the form submission.
        # request.POST['choice'] will raise a KeyError if 'choice' wasn't in POST data.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form with an error message.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        # Increment the vote count for the selected choice and save it.
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        # reverse() helps avoid having to hardcode a URL in the view.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
