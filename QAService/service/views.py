from symtable import Class

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from service.forms import QuestionForm, AnswerForm
from service.models import Question


class Home(ListView):
    model = Question
    template_name = 'service/home.html'
    paginate_by = 1



class QuestionDetailView(DetailView):
    model = Question
    template_name = 'service/question_detail.html'
    context_object_name = 'question'

    #Возможность добавлять ответы на вопросы
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['answers'] = self.object.answers.all().order_by('-time_create')
        context['form'] = AnswerForm()
        return context

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('login')

        self.object = self.get_object()
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.question = self.object
            answer.save()
            return redirect(self.object.get_absolute_url())
        context = self.get_context_data()
        context['form'] = form
        return self.render_to_response(context)


class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "service/ask_question.html"
    #success_url = reverse_lazy('home') #перенаправление после успешного создания вопроса

    def form_valid(self, form):
        form.instance.author = self.request.user #привязываем пользователя
        return super().form_valid(form)


class RegisterView(CreateView, UserCreationForm):
    form_class = UserCreationForm
    template_name = 'service/registration.html'
    success_url = reverse_lazy('login')

class ProfileView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'service/profile.html'
    context_object_name = 'questions'
    paginate_by = 10  # если хочешь пагинацию

    def get_queryset(self):
        return Question.objects.filter(author=self.request.user).order_by('-time_create')


def page_not_found(request, exception):
    return HttpResponseNotFound("Страница не найдена")

