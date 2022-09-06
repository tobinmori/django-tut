from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View
from django.views.generic.base import TemplateView
from .models import Choice, Question


class CBV(View):
    greeting = 'hello'
    def get(self, request):
        # <view logic>
        return HttpResponse(self.greeting)

class SubclassCBV(CBV):
    greeting = 'hola'        

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

    def options(self, request):
        return HttpResponse("hello")

class ListViewDemo(generic.ListView):
    model = Question
    context_object_name = 'all_questions' # for use in templ

    ## The NAME of the corresponing Template MATTERS - must be {model}_list.html

class DetailViewDemo(generic.DetailView):
    model = Question
    context_object_name = 'question'

    ## The NAME of the corresponing Template MATTERS - must be {model}_detail.html


class QuestionDetailView(generic.DetailView):
    model = Question
    template_name = 'polls/qvdetail.html'

    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Question.objects.order_by('-pub_date')[:5]

    # add xtra context here
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_articles'] = 'extra stuff'
        print(context)
        return context
    
class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

class TestRedirectView(generic.RedirectView):
    # see this if you get Reverse Not Found: https://forum.djangoproject.com/t/reverse-for-login-not-found-login-is-not-a-valid-view-function-or-pattern-name/2396/6
    #url = "https://www.google.com" # will go directly to this URL
    pattern_name = "polls:cbv" # within the app - use this -> namespaced reverse lookup!
    permanent = True # 302 status code, if false will be 301
    query_string = False # pass a query string if avail

class TestTemplateView(generic.TemplateView):
    template_name = "polls/template_view_demo.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'this is a dynamic title'
        return context


###
### CRUD views
###

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class CreateViewDemo(generic.CreateView):
    model = Question
    fields = ['question_text','pub_date']
    success_url = reverse_lazy('polls:show-questions') ## IF you use reverse() things will break since url cannot be calculated at compile time

class UpdateViewDemo(generic.UpdateView):
    model = Question
    fields = ['question_text','pub_date']
    template_name_suffix = '_form_update'
    success_url = reverse_lazy('polls:show-questions') ## IF you use reverse() things will break since url cannot be calculated at compile time




def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        print(reverse('polls:results', args=(question.id,)))
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))